from Core import BareBaseModel, BASE_DIR
from Product.Models.Product_Dto import Product_Dto
import os, json
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import NVARCHAR
from sqlalchemy.ext.asyncio import AsyncSession


class Product(BareBaseModel):
    Name : Mapped[str] = mapped_column(NVARCHAR(100), nullable= False)
    Description : Mapped[str] = mapped_column(NVARCHAR(300), nullable= False)
    Price : Mapped[Decimal] = mapped_column(nullable= False)
    Picture_url : Mapped[str] = mapped_column(NVARCHAR(50), nullable= False)
    Type : Mapped[str] = mapped_column(NVARCHAR(50), nullable= False)
    Brand : Mapped[str] = mapped_column(NVARCHAR(50), nullable= False)
    Quantity_in_stock : Mapped[int] = mapped_column(nullable= False)

    @classmethod
    async def load_product(cls):
        with open(os.path.dirname(BASE_DIR) + '\\Product\\Models\\products.json','r') as file:
            products = json.load(file)
        return products
