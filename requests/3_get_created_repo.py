import requests


def get_created_repo(url, token, owner, repo_name):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/json'
    }

    url = url.format(owner=owner, repo=repo_name)
    response = requests.get(url, headers=headers)

    print("Response status code:", response.status_code)

    if response.status_code == 200:
        repo = response.json()

        assert repo['has_wiki'] == False
        assert repo['private'] == True
        assert repo['name'] == 'repo-created-with-api'
        assert repo['owner']['login'] == owner

        return repo
    else:
        return None


if __name__ == "__main__":
    url = "https://api.github.com/repos/{owner}/{repo}"
    your_token = 'SHA256:Q7Vf2hEm5+RIJ/0BDzvwjBk+PatvTVHagbW1bPkVihw'
    your_github_login = 'Acteonis'
    repo_created_with_api = 'repo-created-with-api'

    repo_info = get_created_repo(url, your_token, your_github_login, repo_created_with_api)
