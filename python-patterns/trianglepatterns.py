def nStarTriangle(n: int) -> None:
    space_count = round(n - 1)
    count = 1
    for row in range(n):
        print(" " * space_count, end="")
        print("*" * count)
        count += 2
        space_count -= 1
            

def nReverseTriangle(n: int) -> None:
    # Initialise 'gap' and 'stars'.
    gap = 0
    stars = 2*n-1
    for i in range(n):
        for j in range(gap):
            print(' ', end="")
        for j in range(gap, gap+stars):
            print('*', end="")

        # End the current row of the pattern.
        print()

        gap += 1
        stars -= 2

def main():
    # nStarTriangle(5)
    nReverseTriangle(5)

if __name__ == "__main__":
    main()