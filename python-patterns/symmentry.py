def symmetry(n: int) -> None:
    for row in range(n):
        stars = "* " * (n - row)
        zeros = "  " * (row * 2)
        print(stars + zeros + stars)
    for row in range(n):
        stars = "* " * (row + 1)
        zeros = "  " * ((n - row - 1) * 2)
        print(stars + zeros + stars)

def reversesymmetry(n: int) -> None:
    for row in range(n -1):
        stars = "* " * (row + 1)
        zeros = "  " * ((n - row - 1) * 2)
        print(stars + zeros + stars)
    for row in range(n):
        stars = "* " * (n - row)
        zeros = "  " * (row * 2)
        print(stars + zeros + stars)

def main():
    symmetry(3)
    reversesymmetry(3)

if __name__ == "__main__":
    main()
