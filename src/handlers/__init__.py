from .index_handler import IndexHandler
from .food_handler import FoodHandler

handlers = [
    (r"/", IndexHandler),
    (r"/food", FoodHandler)
]
