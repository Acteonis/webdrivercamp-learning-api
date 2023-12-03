import requests

def get_with_auth(url, token):
# YOUR CODE HERE
    headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/json'
        }
    r = requests.get(url)
    print("Response status code: ", r.status_code)
    if r.status_code == 200:
        data = r.json()
        num_of_repos = len(r)
        return num_of_repos, r.headers
    else:
        return None, None


if __name__ == "__main__":
    url = "https://api.github.com/user/repos"
    token = 'SHA256:Q7Vf2hEm5+RIJ/0BDzvwjBk+PatvTVHagbW1bPkVihw'
    num_of_repos, headers = get_with_auth(url, token)

    print(f"Total Repos: {num_of_repos}")
    print(f"Response headers: {headers}")