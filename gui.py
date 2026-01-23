from rich import print

def generiere_spielfeld():
    print(farbe("x"))

def farbe(zeichen: str) -> str:
    if zeichen == "x":
        return "[bold red]X[/bold red]"
    if zeichen == "0":
        return "[bold blue]O[/bold blue]"
    return " "

if __name__ == "__main__":
    generiere_spielfeld()

    #grid = [["a" for _ in range(7)] for _ in range(6)]
    grid = [
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " "]
    ]