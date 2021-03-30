import pytest
import os
from Calculator import Calculator


class TestCalculator:

    @pytest.fixture()
    def demo_fxtr_1(self):
        print("\n I am a SIMPLE (non-auto use) fixture")

    @pytest.fixture(scope="class", autouse=True)
    def setup_at_class_level(self, request):
        print("\n I am a CLASS (auto use) fixture")
        print(" I am setting up the overall preconditions for all tests")
        print(" Creating a calculator object in CLASS fixture to be used by all tests")
        request.cls.calculator = Calculator()

        print(" *** CLASS FIXTURE DONE ***")

        def tear_down():
            print("\n I am done with all my tests at the end of the class")
            print(" *** CLASS LEVEL TEAR DOWN COMPLETE ***")

        request.addfinalizer(tear_down)

    @pytest.fixture(scope="function", autouse=True)
    def setup_at_test_level(self, request):
        print("\n I am a FUNCTION (auto use) fixture")
        print(" I am setting up the preconditions for each test")
        print(" *** TEST LEVEL FIXTURE DONE ***")

        def tear_test_down():
            print("\n I am done with this specific test at the end of the test")
            print(" *** TEST LEVEL TEAR DOWN COMPLETE ***")

        request.addfinalizer(tear_test_down)

    @pytest.mark.skip(reason="not a good test")
    def test_add_1(self):
        assert self.calculator.add(0, 0) == 0


    @pytest.mark.skipif(os.name == "nt", reason="not a valid test for this OS")
    def test_add_2(self):
        assert self.calculator.add(1, 1) == 2

    def test_add_3(self, request):
        print("my object id is {}".format(request.instance))
        print("my class id is {}".format(request.cls))

        print("my object id is {}".format(self))
        print("my class id is {}".format(self.__class__))
        assert self.calculator.add(10, 1) == 11



    @pytest.mark.parametrize("a, b, expected", [(0,0,0), (10,10,20), (1,99,100)])
    def test_add_multiple(self, request, a, b, expected):
        print("my object id is {}".format(request.instance))
        print("my class id is {}".format(request.cls))

        print("my object id is {}".format(self))
        print("my class id is {}".format(self.__class__))
        assert self.calculator.add(a, b) == expected

    def test_dont_like_this_number(self):
        with pytest.raises(ValueError):
            self.calculator.dont_like_this_number(13)
            assert False, "The number 13 did not raise a value error"

    @pytest.mark.xfail(reason="adding characters fails, waiting for developer to fix the method")
    def test_add_character(self):
        assert self.calculator.add('x', 'y') == 11

    def test_divide(self, demo_fxtr_1):
        assert self.calculator.divide(4, 2) == 2

    def test_subtract(self):
        assert self.calculator.subtract(4, 2) == 2

