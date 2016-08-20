# -*- coding: utf8 -*-


class settings:
    single_transaction = "http://hqdigi2.eastmoney.com/EM_Quote2010NumericApplication/CompatiblePage.aspx?Type=FS&jsName=js&stk="
    def __init__(self):
        self.url = "test"

x = settings()
print(x.single_transaction)
