import streamlit as st 
import joblib
import numpy as np 

st.title("Salary Prediction App")

st.divider()

st.write("With this app, you can estimation the salaries of the company employees")

years= st.number_input("Enter the years at company:", value = 1, step = 1, min_value = 0)
jobrate = st.number_input("Enter the job rate:", min_value=0.0, value=3.5, step=0.5)

x = [years,jobrate]

model = joblib.load("linearmodel.pkl")

st.divider()

predict = st.button("Press the button to predict the salary")

st.divider()

if predict:

    st.balloons()

    X1 = np.array([x])

    prediction = model.predict(X1)

    st.write(f"The estimated salary is {prediction[0]:.2f} $")


else:
    "Please Press the button for app to make the prediction"