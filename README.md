# Contrastive-Learning-for-Astronomy

## Star-Galaxy-Quasar Separation at Rubin LSST Scale 

Here’s a README-ready version you can drop into your repo:

---

## Dataset

This project uses the dataset from **Chaini et al. (2023, MNRAS 518, 3123–3136)** based on **SDSS DR16** spectroscopic objects (stars, galaxies, quasars) with clean photometry.

For each object we use:

* **Images**: 32×32×5 cutouts in the SDSS ugriz bands (five 32×32 images stacked along the channel axis)
* **Photometric features** (per band):

  * dereddened magnitude (`dered_x`)
  * de Vaucouleurs radius (`deVRad_x`)
  * PSF FWHM (`psffwhm_x`)
  * extinction (`extinction_x`)
  * plus 4 colours: `u-g`, `g-r`, `r-i`, `i-z`

We define a **compactness parameter**:

```text
c = < deVRad_x / psffwhm_x > over x ∈ {u, g, r, i, z}
```

* **Compact sources**: `c < 0.5`
* **Faint sources**: mean magnitude over ugriz > 20

From SDSS DR16 we construct two balanced subsets:

* **Compact set** (`c < 0.5`):

  * 80,000 stars
  * 80,000 galaxies
  * 80,000 quasars

* **Faint + compact set** (`c < 0.5`, mag > 20):

  * 50,000 stars
  * 50,000 galaxies
  * 50,000 quasars

All objects satisfy strict SDSS quality cuts (clean photometry, good spectra, non-saturated, etc.).

---

## Experiments

In all experiments we evaluate two tasks:

1. **Star vs Galaxy** (binary classification)
2. **Star vs Galaxy vs Quasar** (3-class classification)

Each task is run with the **ANN**, **CNN**, and the **ensemble (MargNet)**.

### Experiment 1 – Compact only (matched train/test)

* **Data:** Compact set only (`c < 0.5`)
* **Split:**

  * ~75% train
  * ~12.5% validation
  * ~12.5% test
* **Balance:** Roughly equal numbers of stars, galaxies, quasars in each split
* **Goal:** Measure performance on **compact sources** when train and test distributions match.

---

### Experiment 2 – Faint + compact only (matched train/test)

* **Data:** Faint + compact set (`c < 0.5`, mag > 20)
* **Split:**

  * 80% train
  * 10% validation
  * 10% test
* **Balance:** Equal numbers of stars, galaxies, quasars in each split
* **Goal:** Study performance at **faint, compact magnitudes** (where traditional classifiers degrade).

---

### Experiment 3 – Train on compact, test on faint + compact

* **Train + val:** From the **compact set** (`c < 0.5`), ~75%/12.5%
* **Test:** From the **faint + compact set** (`c < 0.5`, mag > 20), balanced across the three classes
* **Goal:** Test **generalization to fainter sources** when the model is trained only on (typically brighter) compact objects, mimicking future deep surveys (e.g. LSST).



