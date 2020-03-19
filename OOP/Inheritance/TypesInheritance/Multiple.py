class CombustionEngine():  # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine():  # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity


# Child class inherited from CombustionEngine and ElectricEngine


class HybirdEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)


car = HybirdEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
