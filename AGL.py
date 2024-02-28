import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def search_artist_image(artist_name):
    search_query = f"{artist_name} artist"
    search_url = f"https://www.google.com/search?q={quote(search_query)}&tbm=isch"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_elements = soup.find_all('img', {'src': True})

        if img_elements:
            return img_elements[0]['src']
        else:
            print("No image found.")
    else:
        print(f"Failed to retrieve search results. Status code: {response.status_code}")

if __name__ == "__main__":
    artist_name = "Daft Punk"
    image_url = search_artist_image(artist_name)

    if image_url:
        # Code for displaying the image on AGL media tab
        print(f"Displaying image for {artist_name}: {image_url}")
    else:
        print("Failed to retrieve image.")
