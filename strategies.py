from abc import ABC, abstractmethod

# Strategy Interface
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, width, height, length, mass):
        pass

# Concrete Strategy for Bulky Packages
class BulkyPackageStrategy(SortingStrategy):
    def sort(self, width, height, length, mass):
        volume = width * height * length
        return volume >= 1000000 or width >= 150 or height >= 150 or length >= 150

# Concrete Strategy for Heavy Packages
class HeavyPackageStrategy(SortingStrategy):
    def sort(self, width, height, length, mass):
        return mass >= 20

# Context Class
class PackageSorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort(self, width, height, length, mass):
        return self._strategy.sort(width, height, length, mass)
