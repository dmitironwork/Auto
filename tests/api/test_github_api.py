import pytest
#2 from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
#2    api = GitHub()
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exist(github_api):
#2    api = GitHub()
    r = github_api.get_user('abudadamita')
#1    print(r)
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('Auto')
    assert r['total_count'] == 1105264
    assert 'auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert ['total_count'] != 0


#перші тести
#     @pytest.mark.api
# def test_user_exists():
#     api = GitHub()
#     user = api.get_user_defunkt()
#     assert user['login'] == 'defunkt'


# @pytest.mark.api
# def test_user_not_exist():
#     api = GitHub()
#     r = api.get_non_exist_user()
#     #print(r)
#     assert r['message'] == 'Not Found'