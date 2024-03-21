from re import search
import requests
import webbrowser
import random  # Import the random module

def get_random_repo(language=None):
    # base url for github search api
    url = "https://api.github.com/search/repositories"

    # define the search parameters
    query = "language:{}".format(language) if language else 'stars:>1'
    sort = "stars"
    order = "desc"

    # parameters for the search query
    params = {
        'q': query,
        'sort': sort,
        'order': order
    }

    response = requests.get(url, params=params)

    # check if the request was successful
    if response.status_code == 200:
        search_results = response.json()['items']
        if search_results:
            random_repo = random.choice(search_results)
            return random_repo
        else:
            return None
    else:
        print(f"Failed to fetch repos. Status code: {response.status_code}")
        return None
    
def main():
    # prompt user to enter a programming language (optional)
    language = input("Enter a programming language (leave blank for random): ").strip()

    repo = get_random_repo(language=language if language else None)
    if repo:
        print(repo['html_url']) # print the url of the random repo
        # open the url in the default web browser
        webbrowser.open(repo['html_url'])
    else:
        print("No repos found")

if __name__ == "__main__":
    main()
