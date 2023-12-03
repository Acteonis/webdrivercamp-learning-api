import requests


def get_repos(url):
# YOUR CODE HERE
    r = requests.get(url)
    print("Response status code: ", r.status_code)
    if r.status_code == 200:
        data = r.json()
        print("Total Count:", data['total_count'])
        return sorted(data['items'], key=lambda x: x['full_name'])
    else:
        return []

if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=webdrivercamp-learning-python"

    list_of_items = get_repos(url)
    print()

    for item in list_of_items:
        user = item['owner']['login']
        repo = item['name']

        print(f"{user:15}", repo)