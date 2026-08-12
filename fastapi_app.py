from fastapi  import FastAPI
import joblib
import numpy as np
from  pydantic import BaseModel

#Load Model
model = joblib.load("titanic_prediction")

#Initialize FastAPI app
app = FastAPI(
    title = "Titanic Survival Predictor",
    version = "Fresh Release",
)

#Define input data structure(pydantic model for validation)    
class TitanicInput(BaseModel):
    pclass: int
    sex: int
    age: float
    sibsp: int
    parch: int
    fare: float
    embarked: int
    
    
# Home route
@app.get("/")
def root():
    return {"message": "Welcome to the Titanic Survival Prediction API"}   

# prediction endpoint
@app.post("/predict")
def predict_survival(data: TitanicInput):
    # Convert input data to numpy array
    input_array = np.array([[data.pclass, data.sex, data.age, data.sibsp, data.parch, data.fare, data.embarked]])
    
    # Get prediction
    prediction = model.predict(input_array)[0]
    
    #Get probability for both classes
    probability = model.predict_proba(input_array)[0]
    
    # Return the prediction and probability results
    return {
        "prediction": int(prediction),
        "survived": "Yes" if prediction == 1 else "No",
        "probability": {
            "survived": float(probability[1]),
            "not_survived": float(probability[0])
        }
    }