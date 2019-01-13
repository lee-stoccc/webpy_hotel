import time


class Utils(object):
    def strDataToData(self, strData):
        return time.strptime(strData, '%Y-%m-%d')
