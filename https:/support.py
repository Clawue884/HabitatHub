class LifeSupport:
    def __init__(self):
        self.oxygen_level = 100  # dalam persen
        self.water_supply = 100  # dalam liter
    
    def monitor_oxygen(self):
        print(f"Kadar oksigen: {self.oxygen_level}%")
        return self.oxygen_level
    
    def monitor_water(self):
        print(f"Persediaan air: {self.water_supply}L")
        return self.water_supply
    
    def adjust_oxygen(self, amount):
        self.oxygen_level = max(0, min(100, self.oxygen_level + amount))
        print(f"Oksigen diatur ke: {self.oxygen_level}%")
    
    def use_water(self, amount):
        self.water_supply = max(0, self.water_supply - amount)
        print(f"Persediaan air tersisa: {self.water_supply}L")
