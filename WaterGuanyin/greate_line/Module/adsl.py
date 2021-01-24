import os


import time
class Adsl(object):
    # ==============================================================================
    # __init__ : name: adsl名稱
    # ==============================================================================
    def __init__(self):
        self.g_adsl_account = None
        self.name = None
        self.username = None
        self.password = None
    # ==============================================================================
    # set_adsl : 修改adsl設置
    # ==============================================================================
    def set_adsl(self, account):
        self.name = account["name"]
        self.username = account["username"]
        self.password = account["password"]

    # ==============================================================================
    # connect : 寬帶撥號
    # ==============================================================================
    def connect(self):
        cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
        os.system(cmd_str)
        time.sleep(5)

    # ==============================================================================
    # disconnect : 斷開寬帶連接
    # ==============================================================================
    def disconnect(self):
        cmd_str = "rasdial %s /disconnect" % self.name
        os.system(cmd_str)
        time.sleep(5)

    # ==============================================================================
    # reconnect : 重新進行撥號
    # ==============================================================================
    def reconnect(self):
        self.disconnect()
        self.connect()

if __name__ == "__main__":

    obj = Adsl()
    obj.reconnect()
