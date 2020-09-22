import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Data model to parse the request body JSON."""

    # zipcode: int = Field(..., example=3.14)
    # accommodates: int = Field(..., example=-42)
    # room_type: str =
    # bathrooms: float =
    # bedrooms: float =
    # property_type: str =
    # city: str =

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #    """Validate that x1 is a positive number."""
    #    assert value > 0, f'x1 == {value}, must be > 0'
    #    return value


@router.post('/predict')
async def predict(item):
    """
    Predict AirBnB rental prices using app data and home features.
    ### Request Body
    Currently just accepting text input, will be updated to accept 
    ### Response 
    '{prediction}$ per night is an optimal price.' 
"""
    # input will be a dictionary, (item :Item)
    return '{}$ per night is an optimal price.'.format(random.randrange(50, 550, 10))
