import requests
from pprint import pprint


def create_repo(url, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    data = {
        'name': 'repo-created-with-api',
        'private': True,
        'has_wiki': False
    }
    response = requests.post(url, headers=headers, json=data)

    print("Response status code:", response.status_code)

    if response.status_code == 201:
        return response.json()
    else:
        # If the request was not successful, return None
        return None

if __name__ == '__main__':
    url = 'https://api.github.com/user/repos'
    token = "SHA256:Q7Vf2hEm5+RIJ/0BDzvwjBk+PatvTVHagbW1bPkVihw"
    repo = create_repo(url, token)
    pprint(repo)