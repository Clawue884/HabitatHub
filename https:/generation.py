class PowerGeneration:
    def __init__(self):
        self.battery_level = 100  # dalam persen
    
    def generate_power(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Tenaga dihasilkan: {amount}%, Baterai saat ini: {self.battery_level}%")
    
    def consume_power(self, amount):
        self.battery_level = max(0, self.battery_level - amount)
        print(f"Tenaga digunakan: {amount}%, Baterai tersisa: {self.battery_level}%")
    
    def monitor_battery(self):
        print(f"Status baterai: {self.battery_level}%")
        return self.battery_level
