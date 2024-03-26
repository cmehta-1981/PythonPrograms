import pytest


class TestClass:

    @pytest.fixture()               # called decorator & execute before every test method called
    def setup(self):
        print("Launching browser")
        print("Open Browser")
        yield                       # called after each test method executed
        print("Close Browser")

    def test_Login(self, setup):  # setup method called first then called login method
        print("return login")

    def test_Search(self, setup):  # setup method called first then called search  method
        print("return search")

    def test_AdvancedSearch(self, setup):  # setup method called first then called Advanced method
        print("return AdvancedSearch")

    def test_SignUp(self):                  # setup method does not called
        print("return signup")
