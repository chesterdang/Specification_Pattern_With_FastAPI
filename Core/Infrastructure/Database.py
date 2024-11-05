from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

engine = create_async_engine("mysql+asyncmy://root:danh123123123@localhost:3306/python_design_test")
SessionLocal = async_sessionmaker(autocommit = False, autoflush=False, bind= engine)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.aclose()

async def seed_data(db: AsyncSession, o: object, dto: BaseModel, load_function):
    product_results = await db.scalars(select(o))
    if len(product_results.all()) == 0: 
        datas = await load_function()
        for data in datas:
            item = dto(**data)
            db.add(o(**item.model_dump()))
        await db.commit()
        

    
 
