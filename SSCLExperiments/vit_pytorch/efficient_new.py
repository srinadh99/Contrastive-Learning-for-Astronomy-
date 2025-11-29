# efficient_new.py

import torch
from torch import nn
from einops import rearrange
from einops.layers.torch import Rearrange

def pair(t):
    return t if isinstance(t, tuple) else (t, t)

class ViT(nn.Module):
    def __init__(
        self,
        *,
        image_size,
        patch_size,
        num_classes,
        dim,
        transformer,
        pool='cls',
        channels=3
    ):
        super().__init__()
        image_size_h, image_size_w = pair(image_size)
        assert image_size_h % patch_size == 0 and image_size_w % patch_size == 0, \
            'image dimensions must be divisible by the patch size'
        assert pool in {'cls', 'mean'}, 'pool type must be either cls or mean'

        num_patches = (image_size_h // patch_size) * (image_size_w // patch_size)
        patch_dim = channels * patch_size ** 2

        # image → patch embeddings
        self.to_patch_embedding = nn.Sequential(
            Rearrange('b c (h p1) (w p2) -> b (h w) (p1 p2 c)',
                      p1=patch_size, p2=patch_size),
            nn.LayerNorm(patch_dim),
            nn.Linear(patch_dim, dim),
            nn.LayerNorm(dim)
        )

        # pf (24-dim) → CLS token embedding
        self.to_dnn = nn.Sequential(
            nn.Linear(24, 1024),
            nn.ReLU(),
            nn.Dropout(p=0.25),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(p=0.25),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(p=0.25),
            nn.Linear(256, dim),
        )

        self.pos_embedding = nn.Parameter(torch.randn(1, num_patches + 1, dim))
        self.transformer = transformer

        self.pool = pool
        self.to_latent = nn.Identity()

        self.mlp_head = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, num_classes)
        )

    def forward(self, pf, img, return_embedding: bool = False):
        """
        pf:  [B, 24]
        img: [B, C, H, W]

        If return_embedding=True: returns [B, dim] (for contrastive learning)
        Else: returns logits [B, num_classes]
        """
        x = self.to_patch_embedding(img)     # [B, num_patches, dim]
        b, n, _ = x.shape

        # CLS token from pf
        cls_tokens = self.to_dnn(pf.view(b, -1)).unsqueeze(1)  # [B, 1, dim]

        x = torch.cat((cls_tokens, x), dim=1)                  # [B, 1+num_patches, dim]
        x = x + self.pos_embedding[:, : (n + 1)]

        x = self.transformer(x)

        if self.pool == 'mean':
            x = x.mean(dim=1)
        else:
            x = x[:, 0]   # CLS token

        x = self.to_latent(x)  # [B, dim]

        if return_embedding:
            return x

        return self.mlp_head(x)
