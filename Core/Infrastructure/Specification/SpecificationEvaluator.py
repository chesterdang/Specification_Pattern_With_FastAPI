from operator import is_, is_not
from sqlalchemy import Select
from sqlalchemy.orm import selectinload
from Core import Specification


def get_query(query: Select, spec: Specification) -> Select:
    
    if spec.criteria is not None :
        query = query.where(spec.criteria)

    
    if spec.order_by:
        query = query.order_by(spec.order_by)
    elif spec.order_by_desc:
        query = query.order_by(spec.order_by_desc.desc())

   
    if spec.is_distinct:
        query = query.distinct()

   
    if spec.is_paging_enabled:
        query = query.offset(spec.skip).limit(spec.take)

    for include in spec.include:
        query = query.options(selectinload(include))
    for include_string in spec.include_string:
        query = query.options(selectinload(include_string))

    return query