from rich import print

def generiere_spielfeld(grid):
    print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    print("-"*29)
    for zeile in grid:
        print("|" + "|".join(farbe(cell) if cell != "   " else "   " for cell in zeile) + "|")
        print("-"*29)


def farbe(zeichen: str) -> str:
    if zeichen == "x":
        return "[bold red]X[/bold red]"
    if zeichen == "o":
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

def move(grid, zeichen):
    while True:
        try:
            spalte = int(input("In welche Spalte möchtes du deinen Stein setzen? (1-7): "))
            if 1 <= spalte and spalte <= 7:
                for zeile in range(len(grid)-1, -1, -1):
                    if grid[zeile][spalte - 1] == "   ":
                        grid[zeile][spalte - 1] = zeichen
                        return
                print("Diese Spalte ist voll!")
            
            else:
                print("Bitte eine Zahl zwischen 1 und 7 eingeben.")
        except ValueError:
            print("Bitte nur Zahlen eingeben.")
            

if __name__ == "__main__":

    
    #grid = [["a" for _ in range(7)] for _ in range(6)]
    grid = [
        ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
        ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
        ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
        ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
        ["   ", "   ", "   ", "   ", "   ", "   ", "   "],
        ["   ", "   ", "   ", "   ", "   ", "   ", "   "]
    ]
    generiere_spielfeld(grid)
    move()