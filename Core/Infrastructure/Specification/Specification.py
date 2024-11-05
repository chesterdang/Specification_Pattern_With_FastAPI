from sqlalchemy import ColumnElement
from Core import ISpecification

class Specification(ISpecification):
    def __init__(self, criteria: ColumnElement | None):
        self.criteria = criteria
        self.order_by = None
        self.order_by_descending = None
        self.is_distinct = False
        self.is_paging_enabled = False
        self.take = 0
        self.skip = 0
        self.include = list()
        self.include_string = list()

    def apply_paging(self, take: int, skip: int):
        self.take = take
        self.skip = skip
        self.is_paging_enabled = True

    def add_include(self, include):
        self.include.append(include)

    def add_include_string(self, include_string: str):
        self.include_string.append(include_string)

    def add_order_by(self, order_by):
        self.order_by = order_by

    def add_order_by_descending(self, order_by_desc):
        self.order_by_desc = order_by_desc

    def add_is_distinct(self):
        self.is_distinct = True

    
