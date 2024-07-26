import pytest

@pytest.fixture()
def first_fixture():
    print("这是我的第一个fixture")
    return 1

@pytest.fixture()
def second_fixture(first_fixture):
    print("这是我的第二个fixture")
    return first_fixture + 2

def test_case1(first_fixture):
    print("这是我的第一个测试用例")
    r=first_fixture
    print(r)


def test_case2(second_fixture):
    print("这是我的第二个测试用例")
    print(second_fixture)

if __name__=="__main__":
    pytest.main(['-vs','test_pytest7.py'])