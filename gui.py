from rich import print

def generiere_spielfeld(grid):
    print("1 2 3 4 5 6 7")
    for zeile in grid:
        print("|".join(cell if cell != "" else " " for cell in zeile))




def farbe(zeichen: str) -> str:
    if zeichen == "x":
        return "[bold red]X[/bold red]"
    if zeichen == "0":
        return "[bold blue]O[/bold blue]"
    return " "

def input_player():
    spieler = []
    spieler_1 = input("Geben Sie den Namen von Spieler 1 ein: ")
    spieler_2 = input("Geben Sie den Namen von Spieler 2 ein: ")
    spieler.append(spieler_1, spieler_2)
    return(spieler)

if __name__ == "__main__":
    generiere_spielfeld()

    
    #grid = [["a" for _ in range(7)] for _ in range(6)]
    grid = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]
    ]
    generiere_spielfeld(grid)