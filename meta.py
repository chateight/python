class GovermentDesignatedMetaClass(type):
  def __new__(meta,name,bases,attributes):
    if bases != (object,):
      if attributes["population"] < 5000000:
        raise ValueError("This is not Goverment designated city")
    return type.__new__(meta,name,bases,attributes)

class GovermentDesignatedCity(object, metaclass=GovermentDesignatedMetaClass):
  population = None

# 東京都 (政令指定都市)
class Tokyo(GovermentDesignatedCity):
  population = 10000000

# 松山市 (政令指定都市ではない)
class Matsuyama(GovermentDesignatedCity):
  population = 500000
