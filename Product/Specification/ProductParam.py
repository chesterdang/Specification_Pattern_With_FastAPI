from Core import PagingParams


class ProductParams(PagingParams):
    def __init__(self, search: str = '', sort: str | None = None) -> None:
        self._brands: list[str] = []
        self._types: list[str] = []
        self.sort =  sort
        self.search = search

    @property
    def brands(self) -> list[str]:
        return self._brands
    
    @brands.setter
    def brands(self, value: str):
        self._brands = [brand for brand in value.split(',') if brand ]

    @property
    def types(self) -> list[str]:
        return self._types
    
    @types.setter
    def types(self, value: str):
        self._types = [type for type in value.split(',') if type]
