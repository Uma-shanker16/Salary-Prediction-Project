# 💰 Salary Prediction Data Science Project

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Pandas-green)
![Visualization](https://img.shields.io/badge/Visualization-Matplotlib-purple)

This project analyzes employee data and builds a machine learning model to predict annual salaries based on job performance and years of experience. The project demonstrates an end-to-end data analytics workflow including data exploration, cleaning, visualization, modeling, and deployment using Streamlit.

The objective of the project is to understand how factors such as **experience, performance rating, department, and geography** influence employee salaries.

Insights and recommendations are provided on the following key areas:

- **Employee Demographics:** Workforce distribution across gender and countries  
- **Performance Analysis:** Job rate patterns across employees and regions  
- **Department Salary Trends:** Departments with the highest average salaries  
- **Predictive Modeling:** Machine learning model to estimate employee salaries  

The Python notebook used for data exploration and model training can be found here:  
[Analysis_Modelling.ipynb]

The deployed Streamlit application used to predict salaries can be found here:  
[[Streamlit App Link](http://localhost:8501)]

---

# 🚀 Project Demo

### Streamlit Salary Prediction App

<video width="100%" controls>
  <source src="assets/demo.webm" type="video/webm">
</video>

---

# 🖼 Application Preview

![App Screenshot](---[streamlit-app-2026-03-13-09-36-31.webm](https://github.com/user-attachments/assets/4e7adb31-9a9c-4068-9bab-66401e5b65c8))

The Streamlit app allows users to input employee details and receive a predicted salary instantly using a trained machine learning model.




# 🧠 Key Business Questions

This analysis answers the following questions:

• How does **experience influence salary growth**?  
• Does **job performance affect compensation**?  
• Which **departments pay the highest salaries**?  
• Are there **regional performance differences across countries**?

---


# 📊 Dataset Overview

The dataset contains:

**689 employee records**

**15 variables**

Key attributes include:

| Feature | Description |
|------|-------------|
| Gender | Employee gender |
| Department | Organizational department |
| Country | Work location |
| Center | Business unit |
| Years | Years of experience |
| Job Rate | Employee performance rating |
| Overtime Hours | Additional work hours |
| Monthly Salary | Monthly pay |
| Annual Salary | Target variable |

---

# 📈 Key Insights

## Workforce Demographics

- 449 Male employees
- 250 Female employees
- Moderate gender distribution imbalance

---

## Performance Analysis

Average job performance rating:

**3.58**

Performance scores follow a **normal distribution** across employees.

---

## Department Salary Trends

Salary varies significantly by department.

Key finding:

**Human Resources shows the highest average salary.**

---

## Geographic Performance

Countries analyzed:

- Egypt
- Saudi Arabia
- UAE
- Syria
- Lebanon

Key insight:

**Saudi Arabia shows the highest average job performance rating.**

---

# 🤖 Machine Learning Model

### Target Variable

Annual Salary

### Input Features

- Years of Experience
- Job Performance Rating

---

## Train Test Split

```python
from sklearn.model_selection import train_test_split

X = data[['years','job rate']]
y = data['annual salary']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

## Model Training

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

---

## Model Evaluation

```python
from sklearn.metrics import mean_absolute_error

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
```

---

## Save Model

```python
import joblib

joblib.dump(model, "salary_model.pkl")
```

---

# 🌐 Streamlit Application

The Streamlit app enables users to:

• Enter years of experience  
• Enter job performance rating  
• Generate salary predictions instantly  

---

# ▶️ Run the Project

### Install Dependencies

```
pip install -r requirements.txt
```

### Run the Streamlit App

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# 📊 Business Recommendations

### Experience Matters

Salary increases strongly correlate with years of experience.

### Standardize Performance Reviews

Consistent evaluation frameworks improve compensation fairness.

### Monitor Department Salary Gaps

Regular compensation audits ensure pay equity.

### Use Predictive Analytics for HR

Machine learning can support workforce planning and compensation strategy.

---

# ⚠️ Assumptions & Caveats

Several assumptions were made during analysis:

- Missing records were removed
- Duplicate records were excluded
- Only two features were used in prediction
- Dataset size is limited and may not represent broader industry patterns

---

# 🛠 Technologies Used

Python  
Pandas  
NumPy  
Scikit-Learn  
Matplotlib  
Streamlit  

---

# 👨‍💻 Author

**Uma Shanker Chintha**

Data Analyst | Power BI Developer | Python | Machine Learning
