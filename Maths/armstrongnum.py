def Armstrong(num):
    arm_num = 0
    number = num 
    k = len(num)
    while num > 0:
        arm_num = arm_num + (num%10)**k
        num = num // 10
    return number == arm_num


def main():
    print(Armstrong(153))

if __name__ == "__main__":
    main()