from rich import print

def generiere_spielfeld(grid):
    print("1 2 3 4 5 6 7")
    print("_"*15)
    for zeile in grid:
        print("|"+"|".join(cell if cell != "" else " " for cell in zeile)+ "|")
        print("_"*15)

    print(farbe("x"))

def farbe(zeichen: str) -> str:
    if zeichen == "x":
        return "[bold red]X[/bold red]"
    if zeichen == "0":
        return "[bold blue]O[/bold blue]"
    return " "

if __name__ == "__main__":

    #grid = [["a" for _ in range(7)] for _ in range(6)]
    grid = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", "O"],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]
    ]
    generiere_spielfeld(grid)