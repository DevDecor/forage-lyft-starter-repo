from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from car import Car

from engine.capulet_engine import CapuletEngine


class Thovex(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, NubbinBattery(last_service_date),
                         CapuletEngine(last_service_date,
                                       current_mileage, last_service_mileage))
