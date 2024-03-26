import pytest


class TestClass:

    def test_LoginByEmail(self):
        print("This is login by email")
        assert True == True

    def test_LoginByFacebook(self):
        print("This is login by facebook")
        assert 1 == 1

    @pytest.mark.skip
    def test_LoginByTwitter(self):
        print("This is login by twitter")
        assert False == False

    @pytest.mark.skip
    def test_SignUpByEmail(self):
        print("This is SignUp by email")
        assert True == False