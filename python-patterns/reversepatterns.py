def seeding(n: int) -> None:
    for row in range(n):
        for col in range(n - row):
            print("*", end=" ")
        print('\n',end="")

def main():
    seeding(3)

if __name__ == "__main__":
    main()
