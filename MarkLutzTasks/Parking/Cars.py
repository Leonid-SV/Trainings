class Cars:
    def __index__(self, quantity, index_ = 0, waycost = 0, go = True):
        self.quantity = quantity
        self.index_ = index_
        self.waycost = waycost
        self.go = go

class Pplace:
    def __index__(self, number, npp, nppleft = npp):
        self.number = number
        self.npp = npp
        self.nppleft = nppleft