
from models.fuzzy_case1 import run_case as case1
from models.fuzzy_case2 import run_case as case2

def test_case1():
    print("Case 1:", case1(37.5, 8.5, 6))

def test_case2():
    print("Case 2:", case2([36,39], [7,10], [3,9]))

if __name__ == "__main__":
    test_case1()
    test_case2()
