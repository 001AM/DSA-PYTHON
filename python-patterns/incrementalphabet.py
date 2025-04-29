def nLetterTriangle(n: int) -> None:
    for row in range(1, n + 1):
        alphabet = ord('A')  # Start from 'A' for each row
        for col in range(row):
            print(chr(alphabet), end=' ')
            alphabet += 1
        print('\n',end="")

def main():
    nLetterTriangle(3)

if __name__ == "__main__":
    main()