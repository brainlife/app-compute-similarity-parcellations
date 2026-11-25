<h1 align="center">Dice similarity between parcellations</h1>

<p align="center">
  A per-parcel table of Dice similarity coefficients between a parcellation and a reference parcellation.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.612"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.612-blue.svg" alt="Run on brainlife.io"></a>
  <a href="https://github.com/brainlife/app-compute-similarity-parcellations/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

> 📍 **This branch, `v1.0`, is the brainlife.io App Compute dice similarity coefficient between parcels in parcellations** ([doi:10.25663/brainlife.app.612](https://doi.org/10.25663/brainlife.app.612)).

## 🧠 At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes the Dice similarity coefficient of each parcel between a parcellation and a reference parcellation with nibabel and numpy, and outputs a per-parcel csv.**

For each label in the reference image, binarizes that label in both parcellations and computes Dice = 2\|A∩B\|/(\|A\|+\|B\|), writing subjectID, structureID (from the reference label.json), nodeID and dice to parcellation.csv. Both parcellations must be on the same voxel grid and share label values.

| | |
|---|---|
| 📥 **Inputs** | `neuro/parcellation/volume` ×2 |
| 📤 **Outputs** | `neuro/parc-stats` |
| 🐳 **Container** | `brainlife/dipy:1.4.1` |
| ⚙️ **Resources** | 1 CPUs · 16 GB memory · 0.5 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.612](https://doi.org/10.25663/brainlife.app.612) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `parc_compare` | `neuro/parcellation/volume` | yes | This is the path to the parcellation you would like to compare to the reference parcellation. Same voxel grid and label numbering as the reference parcellation. |
| `parc_reference` | `neuro/parcellation/volume` | yes | This is the path to the reference parcellation |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `parc_stats` | `neuro/parc-stats` | parcellation.csv with one row per reference parcel: subjectID, structureID, nodeID and dice coefficient. |

<!-- brainlife-app:end -->

## 🚀 Running the App

### ☁️ On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.612](https://doi.org/10.25663/brainlife.app.612), choose the parcellation you want to evaluate (`parc_compare`) and the reference parcellation (`parc_reference`), both `neuro/parcellation/volume`, and press **Execute**. The App writes a `neuro/parc-stats` dataset (tagged `dice_similarity` and `parcellations`) to your project.

For each label in the reference parcellation, the App binarises that label in both images and computes the Dice coefficient, 2|A∩B| / (|A| + |B|). The two parcellations must be on the same voxel grid and use the same label numbering; parcel names are taken from the reference parcellation's `label.json`.

### 💻 Locally

You need [Singularity/Apptainer](https://apptainer.org/). The App runs in the `brainlife/dipy:1.4.1` container (Python 3 with NiBabel, NumPy and pandas).

1. Clone this repository and check out the released version (`git checkout v1.0`).
2. Create `config.json` with the paths to your inputs (see `config.json.sample`). The subject ID written to the table is read from `_inputs[0].meta.subject`:

   ```json
   {
       "parc_compare": "testdata/compare/parc.nii.gz",
       "parc_reference": "testdata/reference/parc.nii.gz",
       "labels": "testdata/reference/label.json",
       "_inputs": [
           { "meta": { "subject": "sample" } }
       ]
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

### 🧪 Sample data

You can download sample datasets from brainlife.io with the [brainlife CLI](https://github.com/brainlife/cli):

```bash
npm install -g brainlife
bl login
mkdir input
bl dataset download <dataset-id>
```

## 📦 Outputs

```text
parc_stats/
└── parc-stats/
    └── parcellation.csv   one row per reference parcel: subjectID, structureID, nodeID, dice
```

## 🩺 Troubleshooting

- **`something went wrong`**: `parcellation.csv` was not written. Check that both parcellations load, and that the labels in the reference `label.json` match its voxel values.

## 📚 Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Compute dice similarity coefficient between parcels in parcellations. brainlife.io App. [doi:10.25663/brainlife.app.612](https://doi.org/10.25663/brainlife.app.612)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## 👥 Authors

- Brad Caron
- Franco Pestilli (project director)

**Contributors:** Soichi Hayashi

## 💰 Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## ⚖️ License

[MIT](https://github.com/brainlife/app-compute-similarity-parcellations/blob/main/LICENSE).
