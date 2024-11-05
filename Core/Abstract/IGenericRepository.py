from Core.Abstract import ISpecification

from abc import ABC,abstractmethod

class IGenericRepository[T](ABC):

    @abstractmethod
    def get_with_spec(self, spec: ISpecification) -> list[T]:
        pass

    @abstractmethod
    def get_by_id_async(self, id: int)-> T | None:
        pass

    @abstractmethod
    async def get_all_async(self) -> list[T]:
        pass

    @abstractmethod
    def add(self, entity: T):
        pass

    @abstractmethod
    def remove(self, entity: T):
        pass

    @abstractmethod
    def is_exist(self, id: int) -> bool:
        pass

    