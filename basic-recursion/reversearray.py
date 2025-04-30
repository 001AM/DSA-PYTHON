import numpy as np

def reverse_array(n: np.ndarray) -> np.ndarray:
    return n[::-1]

def main():
    arr = np.array([1, 2, 3, 5])
    print(reverse_array(arr))

if __name__ == "__main__":
    main()
