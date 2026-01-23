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

def main():
    print("Hello from 4-gewinnt!")

chars = ["x","o"]

if __name__ == "__main__":
    grid = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", "x", "x", "x", "o", "x", " "],
        ["o", "x", "x", "o", "o", "o", "x"]
    ]
    main()
    if check_horizontal(grid):
        print("gewonnen")
