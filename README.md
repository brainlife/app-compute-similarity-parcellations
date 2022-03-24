[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-brainlife.app.612-blue.svg)](https://doi.org/10.25663/brainlife.app.612)

# Compute dice similarity between parcels within parcellations

This app will compute the dice similarity between parcels within parcellations. This app takes input a parcellation (parc_compare), whose date will be compared to the reference parcellation.
The main output of this app is a .csv file that documents the dice coefficient for each parcel.

### Authors

- Brad Caron (bacaron@iu.edu)

### Contributors

- Soichi Hayashi (hayashis@iu.edu)

### Funding

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

## Running the App

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/brainlife.app.612](https://doi.org/10.25663/brainlife.app.612) via the 'Execute' tab.

### Running Locally (on your machine)

1. git clone this repo

2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
	"parc_compare":	"testdata/compare/parc.nii.gz",
	"parc_reference":	"testdata/reference/parc.nii.gz",
	"labels":	"testdata/ashs/label.json",
	"_inputs": [
			{
					"meta": {
							"subject": "sample"
						}
					}
				]
}
```

### Sample Datasets

You can download sample datasets from Brainlife using [Brainlife CLI](https://github.com/brain-life/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download
```

3. Launch the App by executing 'main'

```bash
./main
```

## Output

The main output of this App is contains one CSV file for the dice coefficient for all parcels found in the parcellation.

#### Product.json

The secondary output of this app is `product.json`. This file allows web interfaces, DB and API calls on the results of the processing.

### Dependencies

This App requires the following libraries when run locally.

  - singularity: https://singularity.lbl.gov/
  - Python3: https://www.python.org/downloads/
  - Nibabel: https://nipy.org/nibabel/
  - Pandas: https://pandas.pydata.org/
  - jsonlab: https://github.com/fangq/jsonlab.git
  - numpy: https://numpy.org/
