from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import random
router = APIRouter()


@router.get('/viz/{string}')
async def viz(placeholder: str):
    """
    placeholder
    
    ### Path Parameter
    placeholder : number

    ### Response
    placeholder string
    """
    string = '{}$ per night is an optimal price.'.format(random.randrange(50, 550, 10))
    # Return Plotly figure as JSON string
    return string
