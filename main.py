import gui

def check_horizontal(grid:list[list:str]) -> bool:
    for char in chars:
        for line in grid:
            counter = 0
            for single_char in line:
                if single_char == char:
                    counter += 1
                else:
                    counter = 0
                if counter == 4:
                    return True
    return False

def check_vertical(grid:list[list:str]) -> bool:
    for char in chars:
        column_counter = 0
        while column_counter < len(grid[0]):
            char_counter = 0
            for line in grid:
                if line[column_counter] == char:
                    char_counter += 1
                else:
                    char_counter = 0
                if char_counter == 4:
                    return True
            column_counter +=1
    return False

def check_diagonal(grid:list[list:str]) -> bool:
    for line in range(3):
        for coulmn in range(4):                #erstes mal auslesen
            value1 = grid[line][coulmn+3]      #[" ", " ", " ", "X", " ", " ", " "],
            value2 = grid[line+1][coulmn+2]    #[" ", " ", "X", " ", " ", " ", " "],
            value3 = grid[line+2][coulmn+1]    #[" ", "X", " ", " ", " ", " ", " "],
            value4 = grid[line+3][coulmn]      #["X", " ", " ", " ", " ", " ", " "],
            if value1 == value2 == value3 == value4 and value1 != " ":
                return True
        for coulmn in range(4):                #erstes mal auslesen
            value1 = grid[line][coulmn]        #["X", " ", " ", " ", " ", " ", " "],
            value2 = grid[line+1][coulmn+1]    #[" ", "X", " ", " ", " ", " ", " "],
            value3 = grid[line+2][coulmn+2]    #[" ", " ", "X", " ", " ", " ", " "],
            value4 = grid[line+3][coulmn+3]    #[" ", " ", " ", "X", " ", " ", " "],
            if value1 == value2 == value3 == value4 and value1 != " ":
                return True
    
def unentschieden(grid):
    for line in grid:
        if " " in line:
            return False
    return True
        

def main():
    grid = [["   " for _ in range(7)] for _ in range(6)]
    print("Hello from 4-gewinnt!")
    spieler_liste =gui.input_player()
    while True:
        for i in range(2):
            gui.generiere_spielfeld(grid)
            print(f"Spieler {spieler_liste[i]}: {spieler_liste[i]} ({chars[i]})") 
            gui.move(grid, chars[i])
            if check_horizontal(grid):
                gui.generiere_spielfeld(grid)
                print(f"Spieler {spieler_liste[i]} hat gewonnen!")
                return
            if check_vertical(grid):
                gui.generiere_spielfeld(grid)
                print(f"Spieler {spieler_liste[i]} hat gewonnen!")
                return
            if check_diagonal(grid):
                gui.generiere_spielfeld(grid)
                print(f"Spieler {spieler_liste[i]} hat gewonnen!")
                return


chars = ["x","o"]

if __name__ == "__main__":
    grid = [
        ["o", " ", " ", " ", " ", " ", " "],
        ["o", "o", " ", " ", " ", " ", " "],
        ["x", "o", "o", " ", " ", " ", " "],
        ["x", "x", "o", " ", " ", " ", " "],
        ["x", "x", "x", "o", "o", "x", " "],
        ["o", "x", "x", "o", "o", "o", "x"]

    ]
    main()
    if check_horizontal(grid):
        print("gewonnen vertical")
    if check_vertical(grid):
        print("gewonnen horizontal")
    if check_diagonal(grid):
        print("gewonnen diagonal")
