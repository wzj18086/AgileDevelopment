import types


class MapSettingStrategy:
    def __init__(self, func=None):
        self.func = func

    def execute(self):
        data, layout = self.func
        return data, layout
