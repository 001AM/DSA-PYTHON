def nNumberTriangle(n: int) -> None:
    for row in range(n):
        for col in range(n - row):
            print(col + 1, end=" ")
        print('\n',end="")

def main():
    nNumberTriangle(4)

if __name__ == "__main__":
    main()