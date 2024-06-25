from app.db.models.orders import Order
from app.repositories.base import Repository

order_repository = Repository(Order)
