# print("Hello")

# print("__name__ value: ", __name__)


def calculation(a, b):
    c = a + b
    return c


def outcome(number):
    sentence = "The outcome is " + str(number)
    return sentence


def main():
    print("python main function")
    print(calculation(3, 4))
    print(outcome(calculation(6, 7)))


if __name__ == '__main__':
    main()
