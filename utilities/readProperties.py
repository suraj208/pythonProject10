import configparser
config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Readconfig():
    @staticmethod
    def get_URL(self):
        url=config.get('common file','baseurl')
        return url

