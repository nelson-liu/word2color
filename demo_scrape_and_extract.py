import os

from average_colors import color_kmeans
from scrape_bing import scrape_bing
import webcolors

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def main():
    query = 'yellow'

    # Fetch images and store in images/<query>
    scraper = scrape_bing.BingScraper()
    scraper.download_images(query, 3)

    # Get list of resulting images
    images = map(lambda x: 'images/' + query + '/' + x, os.listdir('images/' + query))

    average_color = color_kmeans.get_average_colors(images)
    print average_color

    actual_name, closest_name = get_colour_name(tuple(average_color))

    print "Actual colour name:", actual_name, ", closest colour name:", closest_name

if __name__ == '__main__':
    main()
