                            
# Function to check if a
# given integer is a palindrome
def palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    return x == reversed_half or x == reversed_half // 10
        


def main():
    number = 4554

    if palindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")


if __name__ == "__main__":
    main()
                           
                        