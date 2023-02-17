import pytest
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_nit_exists(github_api):
    r = github_api.get_user('oleksandryevdokimov')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r= github_api.search_repo("become-qa-auto")
    assert r['total_count'] == 31
    assert 'become-qa-auto' in r['items'][0]['name'] 

@pytest.mark.api
def test_repo_cant_be_found(github_api):
    r= github_api.search_repo("ahebagamingx3duo")
    assert r['total_count'] == 0