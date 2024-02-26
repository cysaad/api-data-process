import numpy as np
from joblib import load
import streamlit as st

# Assuming HeartDiseaseModelInput is a data class or similar structure you have defined elsewhere

# Load the pre-trained models
try:
    loaded_models = {
        'decision_tree': load('DecisionTreeClassifier.joblib'),
        'random_forest': load('RandomForestClassifier.joblib'),
    }
except FileNotFoundError as e:
    st.error(f"Error loading models: {e}")
    # Using st.stop() to halt the app if models cannot be loaded
    st.stop()

# Function to convert user inputs into numerical data
def get_numeric_input(user_input):
    try:
        return float(user_input)
    except ValueError:
        return None

# Prediction function corrected for input handling
def predict(model_type: str, input_data):
    if model_type not in loaded_models:
        return {"prediction": "Model type not supported"}

    # Convert the input data into an array for the model
    input_array = np.array([input_data])

    # Make the prediction
    model = loaded_models[model_type]
    prediction = model.predict(input_array)

    # Return the prediction result
    result = "The person has no heart disease" if prediction[0] == 0 else "The person has heart disease"
    return {"prediction": result}
  
def main():
    st.title('Heart Disease Prediction Web App')
    
    # Getting the input data from the user
    model_type = st.selectbox("Choose the model for prediction", ['random_forest', 'decision_tree'])
    inputs = []
    for field in ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]:
        user_input = st.text_input(f'Enter {field}', key=field)
        numeric_input = get_numeric_input(user_input)
        if numeric_input is None:
            st.error(f"Invalid input for {field}, please enter a number.")
            st.stop()
        inputs.append(numeric_input)
    
    if st.button('Heart Disease Prediction'):
        diagnosis = predict(model_type, inputs)
        st.success(diagnosis['prediction'])

if __name__ == "__main__":
    main()

    
    