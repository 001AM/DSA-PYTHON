'''
    Time Complexity : O( N*N )
    Space complexity: O( 1 )

    Where N is the given input.
'''


def nTriangle(n: int) -> None:
    # For loop 'row' in range 0 to N-1.
    for row in range(n):
        # For loop 'col' in range 0 to N-1.
        for col in range(row+1):
            # Assign forest(row,col) with '*'.
            print('* ', end="")
        print('\n',end="")

def main():
    nTriangle(3)

if __name__ == "__main__":
    main()
