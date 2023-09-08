from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from car import Car

from engine.willoughby_engine import WilloughbyEngine


class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, NubbinBattery(last_service_date),
                         WilloughbyEngine(last_service_date,
                                       current_mileage, last_service_mileage))
