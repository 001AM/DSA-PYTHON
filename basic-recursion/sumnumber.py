def sumNumber(n: int) -> None:
    sum = 0
    for i in range(1,n + 1):
        print(sum,i)
        sum = sum + i

    print(sum)
    sum_formule = n * (n + 1) / 2;

def main():
    sumNumber(3)

if __name__ == "__main__":
    main()
