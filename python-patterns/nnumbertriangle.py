def nTriangle(n:int) ->None:
    for row in range(n): 
        for i in range(row + 1):
            print(i +  1, end=" ")
        print(end='\n')

def main():
    nTriangle(3)

if __name__ == "__main__":
    main()
