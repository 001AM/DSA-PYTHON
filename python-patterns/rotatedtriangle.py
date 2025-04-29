def nStarTriangle(n: int) -> None:
    for rows in range(n):
        for col in range(rows + 1):
            print("*", end=" ")
        print()
    for rows in range(n):
        for col in range(n - rows):
            print("*", end=" ")
        print()

def main():
    nStarTriangle(3)

if __name__ == "__main__":
    main()
