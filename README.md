# Contrastive-Learning-for-Astronomy

## Star-Galaxy-Quasar Separation at Rubin LSST Scale 

More details about the dataset can be found in **[MargFormer](https://github.com/srinadh99/AstroFormer)**

*   **Task:** Star-Galaxy-Quasar classification.
*   **Description:** `SimCLR with MargFormer` is the specific implementation tailored for the SG/SGQ classification tasks. It utilizes a cross-attention mechanism where photometric features (queries) probe image patch embeddings (keys/values), allowing for unified processing of two data types (photometry and FITS images).
*   **Dataset:** The model is developed and evaluated using data products from the **Sloan Digital Sky Survey (SDSS) Data Release 16 (DR16)**. This includes:
    *   Derived photometric features (magnitudes, colors, etc.).
    *   Corresponding FITS images in u, g, r, i, z filters.
    *   Ground-truth spectroscopic classifications from the official SDSS pipeline.
    *   Two specific datasets are generated based on the methodology in [2]:
        *   **Compact source dataset:** Contains relatively brighter sources identified as compact based on criteria described in [2].
        *   **Faint and Compact source dataset:** Contains sources that are both faint (average magnitude > 20) and compact.
*   **Focus:** The evaluation specifically targets challenging populations of faint and compact objects.
*   **Experimental Setup:** To rigorously evaluate performance and generalization, we replicate the three experimental scenarios defined in [2]:
    *   **Experiment 1:**
        *   **Training & Validation:** Compact source dataset.
        *   **Testing:** Compact source dataset.
        
    *   **Experiment 2:**
        *   **Training & Validation:** Faint and Compact source dataset.
        *   **Testing:** Faint and Compact source dataset.
        
    *   **Experiment 3:**
        *   **Training & Validation:** Compact source dataset.
        *   **Testing:** Faint and Compact source dataset.
        *   Critically assess the model's ability to generalize from the brighter compact training regime to the more challenging faint and compact testing regime, simulating real-world application scenarios.
* 
