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
    while True:
        spieler_1 = input("Geben Sie den Namen von Spieler 1 ein: ").strip()
        spieler_2 = input("Geben Sie den Namen von Spieler 2 ein: ").strip()
        
        if not spieler_1:
            print("Spieler 1 darf nicht leer sein.")
            continue
        if not spieler_2:
            print("Spieler 2 darf nicht leer sein.")
            continue
        if spieler_1 == spieler_2:
            print("Die Spielernamen müssen unterschiedlich sein.")
            continue

        return [spieler_1, spieler_2]

        

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