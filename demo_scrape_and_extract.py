import os

from average_colors import color_kmeans
from scrape_bing import scrape_bing

def main():
    query = 'tortie'

    # Fetch images and store in images/<query>
    scraper = scrape_bing.BingScraper()
    scraper.download_images(query, 3)

    # Get list of resulting images
    images = map(lambda x: 'images/' + query + '/' + x, os.listdir('images/' + query))

    average_color = color_kmeans.get_average_colors(images)
    print average_color

if __name__ == '__main__':
    main()
