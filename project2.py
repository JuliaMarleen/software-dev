print("Hello")

print("__name__ value: ", __name__)


def calculation(a, b):
    c = a + b
    return c


def main():
    print("python main function")
    print(calculation(3, 4))


if __name__ == '__main__':
    main()
