from Core import SessionLocal, get_db, seed_data, Base, engine
from contextlib import asynccontextmanager
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, FastAPI

from Product import Product, Product_Dto


@asynccontextmanager 
async def lifespan(app: FastAPI):
    
    db = SessionLocal()
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all) 
            await seed_data(db,Product, Product_Dto,Product.load_product)
        yield db

    finally:
        await db.aclose()

db = Annotated[AsyncSession, Depends(get_db)]

app = FastAPI(lifespan= lifespan)

app.include_router(Product.API.Router.router)
