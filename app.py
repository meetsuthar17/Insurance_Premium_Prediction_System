import streamlit as st
import pickle
import numpy as np


# Load Models
linear_model = pickle.load(open("linear_model.pkl", "rb"))

decision_tree_model = pickle.load(open("decision_tree_model.pkl", "rb"))


# Title
st.title("Insurance Charges Prediction")


# Sidebar
st.sidebar.header("Choose Model")

model_option = st.sidebar.selectbox(

    "Select Model",

    ("Linear Regression", "Decision Tree")

)


# User Inputs
age = st.number_input("Enter Age", min_value=1, max_value=100)

sex = st.selectbox("Select Gender", ["Male", "Female"])

bmi = st.number_input("Enter BMI")

children = st.number_input("Number of Children", min_value=0)

smoker = st.selectbox("Smoker", ["Yes", "No"])

region = st.selectbox(

    "Region",

    ["southwest", "southeast", "northwest", "northeast"]

)


# Encoding Inputs

# sex
if sex == "Male":
    sex = 1
else:
    sex = 0


# smoker
if smoker == "Yes":
    smoker = 1
else:
    smoker = 0


# region
region_dict = {

    "northeast": 0,
    "northwest": 1,
    "southeast": 2,
    "southwest": 3

}

region = region_dict[region]


# Prediction Button
if st.button("Predict Insurance Charges"):


    data = np.array([

        age,
        sex,
        bmi,
        children,
        smoker,
        region

    ]).reshape(1, -1)


    # Model Selection
    if model_option == "Linear Regression":

        prediction = linear_model.predict(data)

    else:

        prediction = decision_tree_model.predict(data)


    # Display Prediction
    st.success(f"Predicted Charges: ${prediction[0]:.2f}")