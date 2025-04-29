def alphaHill(n: int) -> None:
    space_count = n - 1
    for rows in range(n):
        alpha = ord("A")
        print("  " * space_count,end="")
        for col in range(rows + 1):
            print(chr(alpha + col), end=" ")
            # alpha += 1
        
        alpha = ord("A")
        for col in range(rows):
            print(chr(alpha + rows - col - 1), end=" ")
        space_count -= 1
        print()

def main():
    alphaHill(3)

if __name__ == "__main__":
    main()
