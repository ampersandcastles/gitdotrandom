import requests
import webbrowser
import random  # Import the random module

def get_random_repo():
    url = "https://api.github.com/repositories"
    response = requests.get(url)
    repos = response.json()
    # Pick a random repo from the list of repos
    random_repo = random.choice(repos)
    return random_repo

def main():
    repo = get_random_repo()
    print(repo['html_url'])  # Print the URL of the random repo

    # Ensure the returned link opens in the default browser
    webbrowser.open(repo['html_url'])

if __name__ == "__main__":
    main()
