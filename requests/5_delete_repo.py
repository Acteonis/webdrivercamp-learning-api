import requests


def delete_repo(url, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/json'
    }

    response = requests.delete(url, headers=headers)

    print("Response status code:", response.status_code)


if __name__ == '__main__':
    your_token = 'SHA256:Q7Vf2hEm5+RIJ/0BDzvwjBk+PatvTVHagbW1bPkVihw'
    your_github_login = 'Acteonis'
    repo_created_with_api = 'repo-created-with-api'

    url = f'https://api.github.com/repos/{your_github_login}/{repo_created_with_api}'
    delete_repo(url, your_token)