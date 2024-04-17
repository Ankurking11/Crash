import requests
from bs4 import BeautifulSoup
import webbrowser


def usecode():
    print("""Are you sure you wish to use this script?
This will crash you browser and can potientilly crash your system.
""")
    input("Press enter to continue...")

    print("""This is a final warning, that you are proceeding with the script execution.
Press Ctrl+C to exit and end the script
If you still insist, press enter.
Good luck""")

# Function to open every link on a web page
    def open_links(url):

        # Fetch webpage content
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <a> tags (links) in the webpage
        links = soup.find_all('a')
        
        # Loop through each link and open it in a new tab
        # and parse it for new links
        for link in links:
            href = link.get('href')
            if href.startswith('http'):
                webbrowser.open_new_tab(href)
                open_links(href)


    # Example usage:
    url = 'https://www.example.com'
    open_links(url)

usecode()
