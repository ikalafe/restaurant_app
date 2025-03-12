import json

# import MenuItem
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class MenuItem:
    id: int
    name: str
    price: float
    category: str

    def __str__(self) -> str:
        """نمایش آیتم به شکل کاربر پسند"""
        return f"{self.id}: {self.name} - ${self.price:.2f} ({self.category})"

    def __eq__(self, other) -> bool:
        """مقایسه آیتم ها بر اساس شناسه"""
        if not isinstance(other, MenuItem):
            return False
        return self.id == other.id


class Menu:
    def __init__(self, filename: str = "menu.json"):
        self.filename = filename
        self.items: List[MenuItem] = []
        self.load_menu()

    def load_menu(self) -> None:
        try:
            with open(self.filename, "r", encoding="UTF-8") as f:
                data = json.load(f)
                self.items = [MenuItem(**item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.items

    def save_menu(self) -> None:
        """ذخیره فایل در JSON"""
        try:
            with open(self.filename, "w", encoding="UTF-8") as f:
                json.dump([item.__dict__ for item in self.items], f, indent=4)
        except Exception as e:
            print(f"خطا در ذخیره سازی: {e}")

    def add_item(self, name: str, price: float, category: str) -> None:
        """اضافه کردن آیتم جدید به منو"""
        new_id = max([item.id for item in self.items], default=0) + 1
        item = MenuItem(new_id, name, price, category)
        self.items.append(item)
        self.save_menu()
        print(f"Item {name} added successfully")

    def remove_item(self, id: int) -> None:
        """ " حذف آیتم با شناسه مشخص"""
        item = self._find_item(id)
        if item:
            self.items.remove(item)
            self.save_menu()
            print(f"Item with ID {id} found")
        else:
            print(f"آیتم با شناسه {id} پیدا نشد")

    def edit_item(
        self,
        id: int,
        name: Optional[str] = None,
        price: Optional[float] = None,
        category: Optional[str] = None,
    ) -> None:
        """ویرایش آیتم با شناسه مشخص"""
        item = self._find_item(id)
        if item:
            if name:
                item.name = name
            if price is not None:
                item.price = price
            if category:
                item.category = category
            self.save_menu()
            print(f"Item with ID {id} was edited")
        else:
            print(f"Item with ID {id} not found")

    def show_menu(self) -> None:
        """نمایش آیتم های منو"""
        if not self.items:
            print("Menu is Empty")
        else:
            for item in self.items:
                print(item)

    def _find_item(self, id: int) -> Optional[MenuItem]:
        """جستجوی آیتم با شناسه مشخص"""
        for item in self.items:
            if item.id == id:
                return item
        return None
