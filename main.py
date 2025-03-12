import argparse
from Menu import Menu


def main():
    parser = argparse.ArgumentParser(
        description="Restaurant console application",
        epilog="For more information, use the 'help' command.",
    )
    subparser = parser.add_subparsers(dest="command", help="Main commands")

    # دستورات منو
    menu_parser = subparser.add_parser("menu", help="Menu management")
    menu_subparsers = menu_parser.add_subparsers(
        dest="menu_command", help="Menu commands"
    )

    # اضافه کردن آیتم
    add_parser = menu_subparsers.add_parser("add", help="Add a new item to the menu")
    add_parser.add_argument("--name", required=True)
    add_parser.add_argument("--price", type=float, required=True)
    add_parser.add_argument("--category", required=True)

    # حذف آیتم
    remove_parser = menu_subparsers.add_parser("remove", help="Remove item from menu")
    remove_parser.add_argument("--id", type=int, required=True)

    # ویرایش آیتم
    edit_parser = menu_subparsers.add_parser("edit", help="Edit an existing menu item")
    edit_parser.add_argument("--id", type=int, required=True)
    edit_parser.add_argument("--name", required=True)
    edit_parser.add_argument("--price", type=float)
    edit_parser.add_argument("--category")

    # نمایش منو
    show_parser = menu_subparsers.add_parser("show", help="Show all menu items")

    help_parser = subparser.add_parser("help", help="Show program help")

    args = parser.parse_args()

    menu = Menu()

    if args.command == "menu":
        if args.menu_command == "add":
            menu.add_item(args.name, args.price, args.category)
        elif args.menu_command == "remove":
            menu.remove_item(args.id)
        elif args.menu_command == "edit":
            menu.edit_item(args.id, args.name, args.price, args.category)
        elif args.menu_command == "show":
            menu.show_menu()
        else:
            menu_parser.print_help()
    elif args.command == "help":
        parser.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
