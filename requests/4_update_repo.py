import requests


def update_repo(url, token, new_description):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    data = {
        'description': new_description
    }

    response = requests.patch(url, headers=headers, json=data)

    print("Response status code:", response.status_code)
    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == '__main__':
    url = 'https://api.github.com/repos/acteonis/repo-created-with-api'
    your_token = 'SHA256:Q7Vf2hEm5+RIJ/0BDzvwjBk+PatvTVHagbW1bPkVihw'
    new_description = 'I know Python Requests!'

    repo = update_repo(url, your_token, new_description)
    assert repo['description'] == new_description
