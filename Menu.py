import json
import MenuItem


class Menu:
    def __init__(self, filename: str = "menu.json"):
        self.filename = filename
        self.items = []
        self.load_menu()

    def load_menu(self) -> None:
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for item in data:
                    self.items.append(
                        MenuItem(
                            item["id"], item["name"], item["price"], item["category"]
                        )
                    )
        except FileNotFoundError:
            pass

    def save_menu(self) -> None:
        with open(self.filename, "w") as f:
            json.dump([item.__dict__ for item in self.items], f)

    def add_item(self, name: str, price: float, category: str) -> None:
        id = len(self.items) + 1
        item = MenuItem(id, name, price, category)
        self.items.append(item)
        self.save_menu()

    def remove_item(self, id: int) -> None:
        self.items = [item for item in self.items if item.id != id]
        self.save_menu()

    def edit_item(
        self, id: int, name: str = None, price: float = None, category: str = None
    ) -> None:
        for item in self.items:
            if item.id == id:
                if name:
                    item.name = name
                if price:
                    item.price = price
                if category:
                    item.category = category

                self.save_menu()
                return

        print(f"آیتمی با id:{id} پیدا نشد")

    def show_menu(self) -> None:
        for item in self.items:
            print(item)
