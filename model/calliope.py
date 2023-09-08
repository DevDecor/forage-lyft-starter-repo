from datetime import datetime
from battery.spindler_battery import SpindlerBattery
from car import Car
from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, SpindlerBattery(last_service_date),
                         CapuletEngine(last_service_date,
                                       current_mileage, last_service_mileage))
        # self.current_mileage = current_mileage
        # self.lastlast_service_mileage = last_service_mileage
    # def needs_service(self):
    #     service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
    #     if service_threshold_date < datetime.today().date() or self.needs_service():
    #         return True
    #     else:
    #         return False
