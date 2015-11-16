from .food_handler import FoodHandler
from .index_handler import IndexHandler

handlers = [
    (r"/food", FoodHandler),
    (r"/", IndexHandler),
]
