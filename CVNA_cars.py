class CVNA_cars:
    vin = ""
    brand =""
    isPurchasePending = False
    isOnDemand = False
    vehicleInventoryType = 0
    year = 0
    vehicleLockType =0
    status = ""
    def car(self):
        self.set_vin("")
        self.set_isPurchasePending(False)
        self.set_isOnDemand(False)
        self.set_vehicleInventoryType(0)
        self.set_year(0)
        self.set_vehicleLockType(0)
        self.set_brand("")
    def car(self, vin2,isPurchasePending2,isOnDemand2,vehicleInventoryType2,vehicleLockType2,year2,brand2):
        self.set_vin(vin2)
        self.set_isPurchasePending(isPurchasePending2)
        self.set_isOnDemand(isOnDemand2)
        self.set_vehicleInventoryType(vehicleInventoryType2)
        self.set_year(year2)
        self.set_vehicleLockType(vehicleLockType2)
        self.set_brand(brand2)
    def set_vin(self,vin2):
        self.vin = vin2
    def set_isPurchasePending(self,isPurchasePending2):
        self.isPurchasePending = isPurchasePending2
    def set_isOnDemand(self,isOnDemand2):
        self.isOnDemand =   isOnDemand2
    def set_vehicleInventoryType(self,vehicleInventoryType2):
        self.vehicleInventoryType = vehicleInventoryType2
    def set_year(self,year2):
        self.year = year2
    def set_vehicleLockType(self,vehicleLockType2):
        self.vehicleLockType = vehicleLockType2
    def set_brand(self,brand2):
        self.brand = brand2
    def set_status(self,status2):
        self.status = status2.strip()
    def toString(self):
        return self.vin +"\t" + self.brand+"\t" +str(self.isPurchasePending) +"\t" + str(self.isOnDemand) +"\t" +str(self.vehicleInventoryType)+"\t"+str(self.year)+"\t"+str(self.vehicleLockType) +"\t"+self.status+"\n"
