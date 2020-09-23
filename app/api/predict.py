import logging

from fastapi import APIRouter
import joblib
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field, validator
# import pickle


log = logging.getLogger(__name__)
router = APIRouter()


model = joblib.load("app/api/adaboost.joblib")


class Property(BaseModel):
    """Data model to parse the request body JSON."""

    beds: int = Field(...)
    bed_type: str = Field(...)
    bathrooms: float = Field(...)
    bedrooms: float = Field(...) 
    accommodates: int = Field(...)
    room_type: int = Field(...)
    cancellation_policy: str = Field(...)
    property_type: int = Field(...)

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('accommodates')
    # TODO - add more validators?
    def accommodates_must_be_positive(cls, value):
        """Validate that accomodates is a positive number."""
        assert value > 0, f'accommodates == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(property: Property):
    """Predict AirBnB rental prices using app data and home features.

    ### Request body
    - beds: int
    - bed_type: str
    - bathrooms: float
    - bedrooms: float 
    - accommodates: int
    - room_type: int
    - cancellation_policy: str
    - property_type: int


    ### Response 
    '{prediction}$ per night is an optimal price.' 
"""
    prediction = model.predict(property.to_df())
    price = np.exp(prediction[0]) 
    return '{}$ per night is an optimal price.'.format(round(price))


@router.get('/get/{predict}')
async def get_predict(property: Property):
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
    prediction = model.predict(property.to_df())
    price = np.exp(prediction[0]) 
    return '{}$ per night is an optimal price.'.format(round(price))
