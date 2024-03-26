import pytest


class TestClass:

    @pytest.mark.run(order = 4)
    def test_LoginByEmail(self):
        print("This is login by email")
        assert True == True

    @pytest.mark.run(order = 3)
    def test_LoginByFacebook(self):
        print("This is login by facebook")
        assert 1 == 1

    @pytest.mark.run(order = 2)
    def test_LoginByTwitter(self):
        print("This is login by twitter")
        assert False == False

    @pytest.mark.run(order = 1)
    def test_SignUpByEmail(self):
        print("This is SignUp by mobile")
        assert True == True