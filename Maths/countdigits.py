def countDigits(n: int) -> None:
    import math
    print(int(math.log10(n)+1))

def main():
    countDigits(3)

if __name__ == "__main__":
    main()