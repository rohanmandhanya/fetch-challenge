from pydantic import BaseModel, validator
from typing import List


class Item(BaseModel):
    shortDescription: str
    price: str


class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: List[Item]
    total: str

    @validator("items", pre=True)
    @classmethod
    def len_item(cls, value):
        if len(value) < 1:
            raise ValueError("need atleast one item")

        return value
