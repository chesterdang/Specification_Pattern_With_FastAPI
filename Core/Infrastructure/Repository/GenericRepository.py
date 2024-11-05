from Core import IGenericRepository, ISpecification, Base
from Core.Infrastructure.Specification.SpecificationEvaluator import get_query
from typing import TypeVar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


T = TypeVar('T', bound=Base)
class GenericRepository[T](IGenericRepository):
    
    def __init__(self, db:AsyncSession, model: T):
        self.db = db
        self.model = model

    async def get_with_spec(self, spec: ISpecification) -> list[T]:
        result =  await self.db.scalars(get_query(select(self.model), spec)) # type: ignore
        return result.all()

    async def get_by_id_async(self, id: int) -> T | None:
        result =  await self.db.execute(select(self.model).filter_by(Id = id)) # type: ignore
        return result.scalar_one()
    
    async def get_all_async(self) -> list[T]:
        result = await self.db.execute(select(self.model)) # type: ignore
        items = result.scalars().all()
        return items
    
    async def add(self, entity: T) :
        self.db.add(entity)
        await self.db.commit()

    async def remove(self, entity: T) :
        await self.db.delete(entity)
        

    async def is_exist(self, id: int) -> bool:
        result = await self.db.scalars(select(self.model).filter_by(Id = id)) # type: ignore
        return result is not None


