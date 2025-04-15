
import argparse
from models import fuzzy_case1, fuzzy_case2

def main():
    parser = argparse.ArgumentParser(description="Fuzzy Urgency Inference System")
    parser.add_argument('--case', type=int, choices=[1, 2], required=True)
    parser.add_argument('--temperature', type=float, nargs='*')
    parser.add_argument('--headache', type=float, nargs='*')
    parser.add_argument('--age', type=float, nargs='*')
    args = parser.parse_args()

    if args.case == 1:
        result = fuzzy_case1.run_case(args.temperature[0], args.headache[0], args.age[0])
    else:
        result = fuzzy_case2.run_case(args.temperature, args.headache, args.age)

    print(f"Urgency Score: {result}")

if __name__ == "__main__":
    main()
