from pydantic import BaseModel, PositiveFloat, EmailStr,Field
from enum import Enum
from datetime import datetime
from typing import Optional

# class CategoriaBase(Enum):

#BaseModel = Faz todas as validações automaticas pelo pydantic
class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at : datetime

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None
    