class PagingParams:
    def __init__(self, page_index, page_size) -> None:
        self._page_index = page_index
        self._page_size = page_size
        self.max_page_size = 50
    

    @property
    def page_index(self):
        return self._page_index
    
    @page_index.setter
    def page_index(self, value: int):
        self._page_index = value

    @property
    def page_size(self):
        return self._page_size
    
    @page_size.setter
    def page_size(self, value: int):
        self._page_size = value