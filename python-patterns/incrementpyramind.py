def nNumberTriangle(n: int) -> None:
    num : int = 1
    for row in range(1, n + 1):
        # Print left half: 1 to row
        for col in range(row):
            print(num, end=' ')
            num += 1
        print('\n',end="")

def main():
    nNumberTriangle(3)

if __name__ == "__main__":
    main()