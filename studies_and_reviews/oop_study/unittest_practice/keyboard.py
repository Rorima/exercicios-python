class MusicalKeyboard:

    def __init__(self, brand, model, color, keys):
        self.brand = brand.upper()
        self.model = model.upper()
        self.color = color.capitalize()
        self.keys = keys

    def display_brand(self):
        return self.brand

    def display_model(self):
        return self.model

    def display_color(self):
        return self.color

    def display_keys(self):
        return self.keys

    def change_color(self, color_name):
        self.color = color_name
        return f'The color was successfully changed to {color_name.lower()}!'
