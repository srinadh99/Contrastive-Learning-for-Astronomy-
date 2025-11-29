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

### Performance Metrics

Table 1 summarizes the key classification metrics: Accuracy, Precision, and Recall, averaged over 3 independent runs to estimate uncertainty.

**Table 1: MargFormer Classification Performance Metrics**

| Experiment | Classification Task | Accuracy (%) | Precision (%) | Recall (%) |
|---|---|---|---|---|
| **Experiment 1** | Star-Galaxy | 98.1 ± 0.1 | 98.1 ± 0.1 | 98.1 ± 0.1 |
| Compact Train/Test | Star-Galaxy-Quasar | 93.2 ± 0.1 | 93.3 ± 0.1 | 93.2 ± 0.1 |
| **Experiment 2** | Star-Galaxy | 97.1 ± 0.1 | 97.1 ± 0.1 | 97.1 ± 0.1 |
| Faint+Compact Train/Test | Star-Galaxy-Quasar | 86.7 ± 0.1 | 86.8 ± 0.1 | 86.7 ± 0.1 |
| **Experiment 3** | Star-Galaxy | 92.7 ± 0.1 | 93.2 ± 0.1 | 92.7 ± 0.1 |
| Compact Train, Faint+Compact Test | Star-Galaxy-Quasar | 75.2 ± 0.1 | 77.9 ± 0.1 | 75.3 ± 0.1 |




| Experiment | Classification Task | Model  | Accuracy (%)    | Precision (%)   | Recall (%)      |
|-----------|----------------------|--------|-----------------|-----------------|-----------------|
| **Experiment 1** | Star-Galaxy            | MargNet | 98.1 ± 0.1      | 98.1 ± 0.1      | 98.1 ± 0.1      |
| Compact Train/Test | Star-Galaxy-Quasar   | MargNet | 93.2 ± 0.1      | 93.3 ± 0.1      | 93.2 ± 0.1      |
| **Experiment 2** | Star-Galaxy            | MargNet | 97.1 ± 0.1      | 97.1 ± 0.1      | 97.1 ± 0.1      |
| Faint+Compact Train/Test | Star-Galaxy-Quasar | MargNet | 86.7 ± 0.1      | 86.8 ± 0.1      | 86.7 ± 0.1      |
| **Experiment 3** | Star-Galaxy            | MargNet | 92.7 ± 0.1      | 93.2 ± 0.1      | 92.7 ± 0.1      |
| Compact Train, Faint+Compact Test | Star-Galaxy-Quasar | MargNet | 75.2 ± 0.1      | 77.9 ± 0.1      | 75.3 ± 0.1      |

| Experiment | Classification Task | Model  | Accuracy (%) | Precision (%) | Recall (%) |
|-----------|----------------------|--------|--------------|---------------|------------|
| **Experiment 1** | Star-Galaxy            | MargNet | 98.1 ± 0.1 | 98.1 ± 0.1 | 98.1 ± 0.1 |
| **Experiment 1** | Star-Galaxy            | SimCLR  | TBD        | TBD        | TBD        |
| Compact Train/Test | Star-Galaxy-Quasar  | MargNet | 93.2 ± 0.1 | 93.3 ± 0.1 | 93.2 ± 0.1 |
| Compact Train/Test | Star-Galaxy-Quasar  | SimCLR  | TBD        | TBD        | TBD        |
| **Experiment 2** | Star-Galaxy            | MargNet | 97.1 ± 0.1 | 97.1 ± 0.1 | 97.1 ± 0.1 |
| **Experiment 2** | Star-Galaxy            | SimCLR  | TBD        | TBD        | TBD        |
| Faint+Compact Train/Test | Star-Galaxy-Quasar | MargNet | 86.7 ± 0.1 | 86.8 ± 0.1 | 86.7 ± 0.1 |
| Faint+Compact Train/Test | Star-Galaxy-Quasar | SimCLR  | TBD        | TBD        | TBD        |
| **Experiment 3** | Star-Galaxy            | MargNet | 92.7 ± 0.1 | 93.2 ± 0.1 | 92.7 ± 0.1 |
| **Experiment 3** | Star-Galaxy            | SimCLR  | TBD        | TBD        | TBD        |
| Compact Train, Faint+Compact Test | Star-Galaxy-Quasar | MargNet | 75.2 ± 0.1 | 77.9 ± 0.1 | 75.3 ± 0.1 |
| Compact Train, Faint+Compact Test | Star-Galaxy-Quasar | SimCLR  | TBD        | TBD        | TBD        |
