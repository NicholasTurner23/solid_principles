class Gold:
    """
    Gold class
    """
    def __init__(self, name):
        self._name = name

    def form(self):
        return f"{self._name} is physical."
    

class Crypto:
    """
    Crypto class
    """
    def __init__(self, name):
        self._name = name

    def form(self):
        return f"{self._name} is virtual."
    

def get_asset_class(asset="gold"):
    """
    Factory
    """
    assets = dict(gold=Gold("Gold"), crypto=Crypto("Bitcoin"))
    return assets[asset]

if __name__ == "__main__":
    g = get_asset_class("gold")
    print(g.form())

    c = get_asset_class("crypto")
    print(c.form())