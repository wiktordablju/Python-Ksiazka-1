def buildCarInfo(brand, model, **carInfo):
    """Tworzy slownik z informacjami o samochodzie"""
    carInfo['brand'] = brand
    carInfo['model'] = model
    return carInfo