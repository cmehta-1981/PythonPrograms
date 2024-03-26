import pytest


class TestClass:

    @pytest.mark.sanity
    def test_LoginByEmail(self):
        print("This is login by email")
        assert True == True

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_LoginByFacebook(self):
        print("This is login by facebook")
        assert 1 == 1

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_LoginByTwitter(self):
        print("This is login by twitter")
        assert False == False

    @pytest.mark.sanity
    def test_SignUpByEmail(self):
        print("This is SignUp by mobile")
        assert True == True