from .json_handler import JsonHandler

class FoodHandler(JsonHandler):
    def get(self):
        self.response['message'] = "Food food food!"
        self.write_json()
