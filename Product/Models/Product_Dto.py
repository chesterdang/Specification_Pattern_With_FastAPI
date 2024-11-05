from decimal import Decimal
from pydantic import Field, BaseModel 

class Product_Dto(BaseModel):
    Name : str = Field(max_length=100)
    Description : str = Field(max_length=300)
    Price : Decimal = Field(ge=0)
    Picture_url : str = Field(max_length=50)
    Type : str = Field(max_length=50)
    Brand : str = Field(max_length=50)
    Quantity_in_stock : int = Field(ge=0)
