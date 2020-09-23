import numpy as np
from fastapi import APIRouter, HTTPException

import joblib
from predict import Property

#router = APIRouter()

#model = joblib.load("app/api/adaboost.joblib")


#@router.get('/get/predict')
#async def predict(property: Property):
"""
    Predict AirBnB rental prices using app data and home features.
    ### Request body
    - beds: int
    - bathrooms: float
    - bedrooms: float 
    - accommodates: int
    - room_type: str
    - cancellation_policy: str
    - property_type: str


    ### Response 
    '{prediction}$ per night is an optimal price.' 
"""
    #prediction = model.predict(property.to_df())
    #price = np.exp(prediction[0]) 
