import pytest


class TestClass:

    @pytest.mark.dependency()
    def test_OpenApp(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_OpenApp'])
    def test_Login(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_Login'])
    def test_Search(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_OpenApp', 'TestClass::test_Login'])
    def test_advSearch(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_OpenApp'])
    def test_logout(self):
        assert True
