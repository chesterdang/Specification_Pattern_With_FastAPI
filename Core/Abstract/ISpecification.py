from abc import ABC, abstractmethod


class ISpecification(ABC):

    @abstractmethod
    def add_include(sellf, include_string: str):
        pass

    @abstractmethod
    def add_order_by(self, order_by):
        pass

    @abstractmethod
    def add_order_by_descending(self, add_order_by_descending):
        pass

    @abstractmethod
    def add_is_distinct(self):
        pass

    @abstractmethod
    def apply_paging(self, take: int, skip: int):
        pass