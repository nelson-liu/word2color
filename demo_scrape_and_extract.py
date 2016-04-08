from average_colors import color_kmeans
from scrape_bing import BingScraper

def main():
    scraper = BingScraper()
    scraper.download_images('blue cream', 3)

if __name__ == '__main__':
    main()
