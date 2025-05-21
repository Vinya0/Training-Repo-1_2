import pytest
class TestClass:

    @pytest.mark.dependency()
    def test_openApp(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_openApp'])
    def test_login(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_search(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_login','TestClass::test_search'])
    def test_advsearch(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_logout(self):
        assert False

# import pytest
#
# @pytest.mark.dependency()
# def test_start():
#     assert True  # This test will pass
#
# @pytest.mark.dependency(depends=["test_start"])
# def test_login():
#     assert True  # Will run only if test_start passes
#
# @pytest.mark.dependency(depends=["test_login"])
# def test_dashboard():
#     assert True  # Will run only if test_login passes
