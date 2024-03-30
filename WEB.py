import requests
from bs4 import BeautifulSoup
import re
import spacy

# Define blocked hosts
BLOCKED_HOSTS = [
    "google.com",
    "youtube.com",
    "twitter.com",
    "linkedin.com",
]

TOTAL_SEARCH_RESULTS = 2

# Function to perform local Google search and extract search results
def local_google_search(query):
    search_results = []
    
    # Perform search
    response = requests.get("https://www.google.com/search", params={"hl": "en", "q": query})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='g')[:TOTAL_SEARCH_RESULTS]
        
        # Extract relevant information from search results
        for result in results:
            title = result.find('h3').get_text() if result.find('h3') else None
            link = result.find('a')['href'] if result.find('a') else None
            content = ' '.join(span.get_text() for span in result.find_all('span'))
            
            # Filter out blocked hosts and incomplete results
            if link and not any(host in link for host in BLOCKED_HOSTS) and title:
                search_results.append({'title': title, 'link': link, 'content': content})
    
    return search_results

# Function to fetch and process web search results
def web_search(query):
    results = local_google_search(query)
    
    # Dummy processing for demonstration
    processed_results = [{'url': result['link'], 'content': result['content']} for result in results]
    
    return processed_results

# Example usage
query = "your search query"
search_results = web_search(query)
print(search_results)
