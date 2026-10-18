from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.models import OrderStatus


class OrderCreate(BaseModel):
    customer_id: str = Field(min_length=1, max_length=64)
    product_id: str = Field(min_length=1, max_length=64)
    quantity: int = Field(gt=0, le=1000)
    total_amount: float = Field(gt=0)


class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    customer_id: str
    product_id: str
    quantity: int
    total_amount: float
    status: OrderStatus
    created_at: datetime
