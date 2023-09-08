from datetime import datetime
from battery.spindler_battery import SpindlerBattery
from car import Car

from engine.willoughby_engine import WilloughbyEngine


class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, SpindlerBattery(last_service_date),
                         WilloughbyEngine(last_service_date,
                                       current_mileage, last_service_mileage))
    # def needs_service(self):
    #     service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
    #     if service_threshold_date < datetime.today().date():
    #         return True
    #     else:
    #         return False
