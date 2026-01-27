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

def main():
    grid = [["   " for _ in range(7)] for _ in range(6)]
    print("Hello from 4-gewinnt!")
    spieler_liste =gui.input_player() 
    gui.generiere_spielfeld(grid)
    gui.move(grid, "x")
    gui.generiere_spielfeld(grid)
    gui.move(grid, "o")
    gui.generiere_spielfeld(grid)

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
