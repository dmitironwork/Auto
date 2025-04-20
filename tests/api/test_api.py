import pytest 


@pytest.mark.api
def test_user_exist(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exist(github_api):
    r = github_api.get_user('abudadamita')
    assert r['message'] == 'Not Found'
 

# import pytest


# class User:
    
#     def __init__(self) -> None:
#         self.name = 'Dmytro'
#         self.second_name = 'Beznosov'

# @pytest.fixture
# def user():
#     yield User()


# def test_remove_name(user):
#     user.name = ''
#     assert user.name == ''

# def test_name(user):
#     assert user.name == 'Dmytro'

# def test_second_name(user):
    # assert user.second_name == 'Beznosov'