from Configuration.Singleton import Singleton
import pandas as pd


class ReadCsv(Singleton):
    global df
    def __init__(self, path):
        self.path = path

    def readCsv(self):
        df_temp = pd.read_csv(self.path)
        return df_temp

    def getCsvData(self):
        df = ReadCsv.readCsv(self)
        lat = df['Latitude']
        lon = df['Longitude']
        store_number = df['Store Number'].fillna('unknown')
        store_name = df['Store Name'].fillna('unknown')
        address = df['Street Address'].fillna('unknown')
        postcode = df['Postcode'].fillna('unknown')
        phone_number = df['Phone Number'].fillna('unknown')
        return lat, lon, store_number, store_name, address, postcode, phone_number

