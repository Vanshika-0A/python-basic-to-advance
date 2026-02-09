class laptop:
    storage_type = "ssd"
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

    def getinfo(self):
        print(f"laptop has {self.ram} ram and {self.storage} {self.storage_type}")
    @classmethod   
    def get_storagetype(cls):
        print(f"storage_type {cls.storage_type}")


    @staticmethod
    def cal_discount(price,discount):
        final_price = price-(discount*price/100)
        print(f"final_price is {final_price}")


l1 = laptop("8gb","256gb")
# l2 = laptop("16gb", "512gb")
# l1.getinfo()
# l2.getinfo()
laptop.cal_discount(40_000,10)
l1.cal_discount(40_000,10)