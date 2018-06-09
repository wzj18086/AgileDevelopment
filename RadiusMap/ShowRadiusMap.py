from GUI import *
from GUI import Initialize
from RadiusMap.RadiusSearch import radiusSearch
from RadiusMap.RadiusTimeChange import radiusTimeChange


def radiusSearchShow():
    x = Initialize.initialize()
    lats = (float)(x.enter_latitude.get())
    lons = (float)(x.enter_longitude.get())
    radius=(float)(x.radius_value.get())
    radiusSearch(lats,lons,radius)

def radiusTimeChangeShow():
    x = Initialize.initialize()
    lats = (float)(x.enter_latitude.get())
    lons = (float)(x.enter_longitude.get())
    radiusTimeChange(lats,lons)