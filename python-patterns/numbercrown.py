def numberCrown(n: int) -> None:
    for row in range(1, n + 1):
        # Print left half: 1 to row
        for col in range(1, row + 1):
            print(col, end=' ')
        
        # Print spaces: 2*(n - row)
        space_count = 2 * (n - row)
        print('  ' * space_count, end='')  # Two spaces per count for alignment
        
        # Print right half: row to 1
        for col in range(row, 0, -1):
            print(col, end=' ')
        
        print()  # New line after each row

def main():
    numberCrown(3)

if __name__ == "__main__":
    main()