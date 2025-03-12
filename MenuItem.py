class MenuItem:
    def __init__(self, id: int, name: str, price: float, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self) -> str:
        return f"{self.id}: {self.name} - {self.price} ({self.category})"
