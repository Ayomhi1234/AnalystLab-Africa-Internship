import streamlit as st
import joblib
import numpy as np

#Load trained model
model = joblib.load("titanic_prediction")

#configure pagge
st.set_page_config(page_title="Titanic Survival Predictor", layout="centered")

#page title and description
st.title("Titanic Survival Predictor")
st.write("Enter the passenger details below to predict survival chances")

# create two columns for layout
col1, col2 = st.columns(2)

#left column inputs
with col1:
    #dropdown for passenger class
    pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3]) 
    
    #slider for age(0, 80, default 30)
    age = st.slider("Age", 0, 80, 30)
    
    #Number input for siblings/spouses aboard 
    sibsp = st.number_input("Number of Siblings/Spouses Aboard", 0,8, 0)
    
    
#right column inputs
with col2:
    #dropdown for sex(convert to 0/1 encoding)
    sex = st.selectbox("Sex", ["Female", "Male"])
    sex_encoded = 0 if sex == "Female" else 1
    
    #number input for ticket fare
    fare = st.number_input("Ticket Fare", 0.0, 500.0, 50.0)
    
    #number input for parents/children 
    parch = st.number_input("Number of Parents/Children Aboard", 0, 6, 0) 
    
# Dropdown for emnbarkation port
embarked_dict = {"Southampton": 0, "Cherbourg": 1, "Queenstown": 2}  # Dictionary
embarked_selected = st.selectbox("Port of Embarkation", list(embarked_dict.keys()))  # Pass list of names
embarked_encoded = embarked_dict[embarked_selected]  # Look up the number

# Create a button to trigger prediction
if st.button("Predict Survival", type="primary"):
     # Create input array from user inputs
    input_data= np.array([[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]])
    
    # Get prediction from the model
    prediction = model.predict(input_data)[0]
    
    #Get prediction probabilities
    probability = model.predict_proba(input_data)[0]    
    
    # Display the prediction result
    if prediction == 1:
        st.success(f"The model predicts that the passenger SURVIVED with a probability of {probability[1]:.2%}.")
        
    else:
        st.error(f"The model predicts that the passenger DID NOT SURVIVE with a probability of {probability[0]:.2%}.")  
    
  # Display survival probability as metric
    st.metric("Survival Probability", f"{probability[1]:.1%}")
