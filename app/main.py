from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serialize import XmlSerializer, JsonSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    print_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    }

    serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display_strategies.get(method_type)
            if strategy:
                strategy.display(book.content)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            strategy = print_strategies.get(method_type)
            if strategy:
                strategy.print(book.title, book.content)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            strategy = serialize_strategies.get(method_type)
            if strategy:
                return strategy.serialize(book.title, book.content)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
