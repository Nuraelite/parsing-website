import requests
from bs4 import BeautifulSoup

def get_news_titles(url):
    # Send a request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all headlines (example for BBC News)
        titles = soup.find_all('h3')  # Headlines are usually in <h3> tags
        
        # Print the headlines
        for index, title in enumerate(titles, start=1):
            print(f"{index}. {title.text.strip()}")
    else:
        print(f"Error: Failed to load the page. Status code: {response.status_code}")

if __name__ == "__main__":
    # Example URL for parsing (BBC News)
    url = "https://www.bbc.com/news"
    print(f"News headlines from {url}:")
    get_news_titles(url)
