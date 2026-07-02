# 💼 Employee Salary Prediction using Machine Learning

## 📌 Overview

This project predicts employee salaries based on demographic and professional information using a Machine Learning Regression model.

The project covers the complete Machine Learning workflow from data exploration to model deployment using Streamlit.

---

## 🚀 Project Workflow

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Feature Engineering
- Model Training
- Model Evaluation
- Model Deployment with Streamlit

---

## 📊 Dataset Features

| Feature | Description |
|----------|-------------|
| Age | Employee age |
| Gender | Employee gender |
| Education Level | Highest education level |
| Job Title | Employee job title |
| Years of Experience | Total years of experience |

### 🎯 Target

- Salary

---

## 🤖 Machine Learning Model

- Linear Regression

---

## 📈 Model Performance

| Metric | Value |
|--------|--------|
| R² Score | **0.8323** |
| MAE | **15,790.97** |
| RMSE | **21,432.77** |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

---

## 📂 Project Structure

```
employee-salary-prediction
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data
│   ├── raw
│   └── processed
│
├── models
│   └── salary_model.pkl
│
├── notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Model_Training.ipynb
│   ├── 05_Model_Evaluation.ipynb
│   └── 06_Deployment.ipynb
│
└── src
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/nouremo77/employee-salary-prediction.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 💡 Future Improvements

- Train and compare multiple regression models
- Hyperparameter tuning
- Cross-validation
- Feature importance analysis
- Deploy the application online using Streamlit Cloud

---

## 👩‍💻 Author

**Nour Ezz Alarab**

AI Engineer | Machine Learning Enthusiast

- GitHub: *https://github.com/nouremo77*
- LinkedIn: *www.linkedin.com/in/nour-ezz-alarab*
