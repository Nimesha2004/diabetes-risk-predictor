# 🩺 Diabetes Risk Predictor

A Machine Learning Classification project built with **Python** and **Scikit-Learn** to predict the risk of diabetes based on key health metrics. This project is designed as part of my hands-on learning journey in Data Science and Machine Learning.

---

## 🚀 Overview

This repository contains a **Logistic Regression** model trained to classify whether a person has a low or high risk of developing diabetes. The model utilizes continuous data to output a binary classification (0 for Low Risk, 1 for High Risk).

### Key Features:
- **Data Preprocessing:** Handled structured data using `Pandas`.
- **Classification Model:** Implemented `LogisticRegression` from `Scikit-Learn`.
- **Interactive UI:** A simple, interactive command-line interface (CLI) for users to test custom inputs dynamically.

---

## 📊 Dataset Structure

The model is trained on a structured dataset (`diabetes_data.csv`) consisting of the following features:

| Feature | Description |
| :--- | :--- |
| **Glucose** | Plasma glucose concentration level |
| **BMI** | Body Mass Index (weight in kg / (height in m)^2) |
| **Age** | Age of the individual (years) |
| **Outcome** | Target Variable (0: Low Risk, 1: High Risk) |

---

## 🛠️ Technologies & Tools Used

- **Language:** Python
- **Libraries:**
  - `pandas` (Data manipulation)
  - `scikit-learn` (Model training and evaluation)

---

## 💻 How to Run the Project

### 1. Prerequisites
Make sure you have Python and the required libraries installed:
bash
```py -m pip install pandas scikit-learn ```

### 2. Execution
python diabetes_project.py

### 3. Sample Input and Output
--- Diabetes Risk Prediction System ---
Enter Glucose Level (mg/dL): 150
Enter BMI (e.g., 25.5): 35
Enter Age: 45

--- Result ---
⚠️ Warning: High risk of Diabetes. Please consult a doctor.

## 📈 Future Improvements
- [ ] Connect a web-based user interface using **Streamlit**.
- [ ] Expand the dataset for better accuracy.
- [ ] Try alternative algorithms like Random Forest or Decision Trees to compare accuracy.

---
💡 *Developed with passion to explore the power of AI & Machine Learning!*
