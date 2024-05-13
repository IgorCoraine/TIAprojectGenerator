class Device:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def __str__(self):
        return f"Name: {self.name}\nModules: {', '.join(self.modules)}"