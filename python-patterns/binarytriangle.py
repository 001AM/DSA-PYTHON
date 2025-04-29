def nBinaryTriangle(n: int) -> None:
    for rows in range(n):
        for col in range(rows + 1):
            if (rows + col) % 2 == 0:
                print("1", end=" ")
            else:
                print("0",end=" ")
        
        print()

def main():
    nBinaryTriangle(3)

if __name__ == "__main__":
    main()
