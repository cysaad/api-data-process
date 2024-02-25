# Heart Disease Prediction Project

## Project Overview
This project aims to develop a machine learning model to predict the presence of heart disease in individuals based on various medical parameters. We use the `heart_data` dataset, which contains clinical measurements related to heart health.

## Dataset Description
The `heart_data` dataset includes the following features:

- `age`: The age of the individual.
- `sex`: The gender of the individual (1 = male; 0 = female).
- `cp`: Chest pain type (0 to 3).
- `trestbps`: Resting blood pressure (in mm Hg on admission to the hospital).
- `chol`: Serum cholesterol in mg/dl.
- `fbs`: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false).
- `restecg`: Resting electrocardiographic results.
- `thalach`: Maximum heart rate achieved.
- `exang`: Exercise-induced angina (1 = yes; 0 = no).
- `oldpeak`: ST depression induced by exercise relative to rest.
- `slope`: The slope of the peak exercise ST segment.
- `ca`: Number of major vessels (0-3) colored by fluoroscopy.
- `thal`: Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect).
- `target`: Presence of heart disease (1 = yes; 0 = no).

## Prerequisites
- Python 3.6 or above
- Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn

## Installation
To set up the project environment, run the following command to install the required packages:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn

## Dataset Source
The dataset was obtained from the UCI Machine Learning Repository:

Janosi, Andras, Steinbrunn, William, Pfisterer, Matthias, and Detrano, Robert. (1988). Heart Disease. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X

BibTeX citation:
```bibtex
@misc{misc_heart_disease_45,
  author       = {Janosi, Andras and Steinbrunn, William and Pfisterer, Matthias and Detrano, Robert},
  title        = {{Heart Disease}},
  year         = {1988},
  howpublished = {UCI Machine Learning Repository},
  note         = {{DOI}: https://doi.org/10.24432/C52P4X}
}
## Models Evaluated
The following machine learning models were evaluated:

Logistic Regression
Decision Tree Classifier
Support Vector Classifier (SVC)
K-Nearest Neighbors (KNN)
Random Forest Classifier
Evaluation Metrics
The models were evaluated based on Accuracy, Precision, Recall, and F1 Score.

## Results
The Random Forest and Decision Tree models demonstrated the highest accuracy in predicting the presence of heart disease.
Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
Heart Disease UCI Dataset from Kaggle
Contributions from the open-source community
