from abc import ABC, abstractmethod


class Car():
    def __init__(self, last_service_date, battery, engine):
        self.last_service_date = last_service_date
        self.battery = battery
        self.engine = engine

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
