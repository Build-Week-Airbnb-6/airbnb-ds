from fastapi import APIRouter
import random

router = APIRouter()


@router.get('/get/test')
async def viz(placeholder: str):
    """placeholder.

    ### Path Parameter
    placeholder : number

    ### Response
    placeholder string
    """
    string = '{}$ per night is an optimal price.'.format(random.randrange(50, 550, 10))
    # Return Plotly figure as JSON string
    return string
