# modeling_tools module

class Model:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return f"Model name is {self.name}"

def transform_data(data):
    return [x * 2 for x in data]

def calculate_average(data):
    return sum(data) / len(data)
