class HabitatAgent:
    def __init__(self, life_support, power_gen, comms):
        self.life_support = life_support
        self.power_gen = power_gen
        self.comms = comms
    
    def perform_daily_checks(self):
        self.life_support.monitor_oxygen()
        self.life_support.monitor_water()
        self.power_gen.monitor_battery()
    
    def emergency_shutdown(self):
        print("Menjalankan prosedur darurat!")
        self.power_gen.consume_power(50)
        self.comms.terminate_connection()
        print("Shutdown selesai.")
