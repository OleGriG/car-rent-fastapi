from fastapi import FastAPI
from .api import auth, cars, orders

app = FastAPI()

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(cars.router, prefix="/api/cars", tags=["cars"])
app.include_router(orders.router, prefix="/api/orders", tags=["orders"])

@app.on_event("startup")
def startup():
    import app.db.session as db_session
    db_session.Base.metadata.create_all(bind=db_session.engine)

