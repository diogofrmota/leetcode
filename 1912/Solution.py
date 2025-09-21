from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: list[list[int]]):
        self.price_map = {}  # (shop, movie) -> price
        self.available = defaultdict(SortedList)  # movie -> SortedList[(price, shop)]
        self.rented = SortedList()  # SortedList[(price, shop, movie)]
        
        for shop, movie, price in entries:
            self.price_map[(shop, movie)] = price
            self.available[movie].add((price, shop))

    def search(self, movie: int) -> list[int]:
        return [shop for price, shop in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_map[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]