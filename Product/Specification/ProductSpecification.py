import Product, ProductParam, Specification

from sqlalchemy import and_, or_
from sqlalchemy.sql.expression import true




class ProductSpecification(Specification):
    def __init__(self, param: ProductParam):

        super().__init__(and_(
            Product.Name.contains(param.search) if param.search else true(),
            Product.Brand.in_(param.brands) if param.brands else true(),
            Product.Type.in_(param.types) if param.types else true())
        )

        self.apply_paging(param.page_size, param.page_size*(param.page_index -1))

        match(param.sort):
            case 'priceAsc':
                self.add_order_by(Product.Price)
            case 'priceDesc':
                self.add_order_by_descending(Product.Price)
            case _:
                self.add_order_by(Product.Name)
