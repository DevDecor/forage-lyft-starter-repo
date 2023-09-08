from datetime import datetime
from battery.spindler_battery import SpindlerBattery
from car import Car

from engine.sternman_engine import SternmanEngine


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date, SpindlerBattery(last_service_date),
                         SternmanEngine(warning_light_is_on))
    # def needs_service(self):
    #     service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
    #     if service_threshold_date < datetime.today().date() or self.needs_service():
    #         return True
    #     else:
    #         return False
