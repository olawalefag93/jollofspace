from fastapi import APIRouter, HTTPException
from . import database, models, schemas
from pydantic import BaseModel

router = APIRouter()

class Message(BaseModel):
    message: str

# ✅ Add this new route:
@router.post("/submit")
async def submit_message(msg: Message):
    return {"response": f"You said: {msg.message}"}

# GET /products – fetch all products
@router.get("/products", response_model=list[schemas.Product])
async def get_products():
    query = models.Product.__table__.select()
    return await database.database.fetch_all(query)

# POST /products – create a new product
@router.post("/products", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate):
    query = models.Product.__table__.insert().values(
        name=product.name,
        description=product.description,
        price=product.price,
        image_url=product.image_url
    )
    product_id = await database.database.execute(query)
    return {**product.dict(), "id": product_id}

