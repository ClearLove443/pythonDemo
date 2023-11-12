from datetime import datetime
from typing import Optional, Tuple

from pydantic import BaseModel


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
    tabs: list


m = Delivery(timestamp="2020-01-02T03:04:05Z", dimensions=["10", "20"])
i = Item(name="t", price=0.1, tabs=["10", "20"])
print(repr(m.timestamp))
# > datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions)
# > (10, 20)
