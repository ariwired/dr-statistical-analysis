![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Objective

This repository contains a practical study of public datasets related to **Diabetic Retinopathy (DR)**, with emphasis on dataset selection, data preprocessing, exploratory analysis, and statistical methods applied to ophthalmological data.

## Project Structure

The project is organized into two main notebooks:

### `00_dataset_comparison.ipynb`

A complementary notebook dedicated to the search and comparison of public datasets related to Diabetic Retinopathy.

The datasets are evaluated according to criteria such as:

* data availability and format;
* number and diversity of variables;
* clinical and demographic information;
* sample size;
* disease outcome/classification;
* documentation and data quality;
* accessibility;
* suitability for statistical analysis.

The comparison supports the selection of the dataset used in the main analysis.

### `01_diabetic_retinopathy_analysis.ipynb`

This notebook contains the **main analysis developed for the Computing Project course activity**.

It follows the requirements proposed in the activity and includes:

* dataset description;
* data cleaning and preprocessing;
* missing value analysis;
* duplicate and inconsistency checks;
* descriptive statistics;
* data visualization;
* correlation analysis;
* comparison between groups;
* statistical hypothesis testing;
* interpretation of results;
* limitations;
* conclusion.

## Data Sources

The datasets investigated during the selection stage are obtained from public repositories, including:

* [Kaggle](https://www.kaggle.com/)
* [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
* [PhysioNet](https://physionet.org/)

The original source of each dataset is identified and referenced in the respective notebook.

## Reproducibility

The analyses are developed in Python using Jupyter Notebook/Google Colab and statistical and data visualization libraries.

All relevant preprocessing and analytical decisions are documented in the notebooks to support reproducibility.

## Repository Structure

```text
.
├── README.md
├── 00_dataset_comparison.ipynb
└── 01_diabetic_retinopathy_analysis.ipynb
```

## Note

The `00_dataset_comparison.ipynb` notebook is a complementary dataset selection study and is not intended to replace the course activity itself.

The `01_diabetic_retinopathy_analysis.ipynb` notebook represents the main analysis submitted for the Computing Project course, using a single dataset selected based on the criteria established during the comparison stage.
