import pytest

class TestClass:

    @pytest.mark.order(3)
    def test_methodC(self):
        print("Running method C.. ")

    @pytest.mark.order(4)
    def test_methodD(self):
        print("Running method D.. ")

    @pytest.mark.order(5)
    def test_methodE(self):
        print("Running method E.. ")

    @pytest.mark.order(1)
    def test_methodA(self):
        print("Running method A.. ")

    @pytest.mark.order(2)
    def test_methodB(self):
        print("Running method B.. ")
