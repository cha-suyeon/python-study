import argparse
from calculator import Calculator


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculator')
    parser.add_argument('num1', type=int, help='First number')
    parser.add_argument('num2', type=int, help='Second number')
    args = parser.parse_args()

    cal = Calculator()

    print("add: ", cal.add(args.num1, args.num2))
    print("sub: ", cal.sub(args.num1, args.num2))
    print("mul: ", cal.mul(args.num1, args.num2))
    print("div: ", cal.div(args.num1, args.num2))