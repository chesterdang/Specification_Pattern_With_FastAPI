from typing import Annotated
from fastapi import APIRouter, Depends, Query
from Product.Models import Product
from Product.Specification import ProductParam, ProductSpecification
from Core import GenericRepository, get_db
from sqlalchemy.ext.asyncio import AsyncSession

route = APIRouter(
    prefix='/product',
    tags=['product']
)
db = Annotated[AsyncSession, Depends(get_db)]

@route.get("/{product_id}")
async def test(data: db, product_id: int):
    a = GenericRepository(data,Product)
    
    return await a.get_by_id_async(product_id) 
    
@route.delete("/{product_id}")
async def test_delete(data: db, product_id: int):
    a = GenericRepository(data, Product)
    p = await a.get_by_id_async(product_id) 
    if p != None:
        await a.remove(p)

@route.get("/spec")
async def test_spec(
    data:db, 
    page_size: int = Query(10, alias='page_size'),
    page_index: int = Query(1, alias='page_index'),
    brands = Query('',alias='brands'),
    types = Query('',alias='types'),
    sort = Query(None, alias='sort'),
    search = Query('', alias='search')
):
    param = ProductParam(search= search, sort= sort)
    param.brands = brands
    param.types = types
    param.page_index = page_index
    param.page_size = page_size

    spec = ProductSpecification(param)
    repo = GenericRepository(data, Product)
    return await repo.get_with_spec(spec= spec)