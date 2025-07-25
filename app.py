import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("decision_tree_model.pkl")

# Page config
st.set_page_config(page_title="Decision Tree Predictor", layout="centered")

st.title("🌳 Decision Tree Classifier")
st.write("Enter input values to predict the class using a trained Decision Tree model.")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", 0.0, 10.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", 0.0, 10.0, step=0.1)

if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    classes = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"🌸 Predicted class: {classes[prediction[0]]}")
