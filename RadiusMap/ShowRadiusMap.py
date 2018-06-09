from GUI import *
from GUI import Initialize
from OtherGraphic.RadiusSearch import *
from OtherGraphic.RadiusTimeChange import radiusTimeChange


def radiusSearch():
    x = Initialize.initialize()
    lats = (float)(x.enter_latidtude.get())
    lons = (float)(x.enter_longitude.get())
    radius=(float)(x.radius_value.get())
    radiusSearch(lats,lons,radius)

def radiusTimeChange():
    x = Initialize.initialize()
    lats = (float)(x.enter_latidtude.get())
    lons = (float)(x.enter_longitude.get())
    radiusTimeChange(lats,lons)