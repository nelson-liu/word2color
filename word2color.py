import os
import shutil
import webcolors

from average_colors import color_kmeans
from scrape_bing import scrape_bing

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.html4_hex_to_names.items():
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


def color_description_to_bin(color):
    color = color.replace('/', ' ')

    # Fetch images and store in images/<color>
    scraper = scrape_bing.BingScraper()
    scraper.download_images(color, 3)

    # Get list of resulting images
    images = map(lambda x: 'images/' + color + '/' + x, os.listdir('images/' + color))

    average_color = color_kmeans.get_average_colors(images)

    actual_name, closest_name = get_colour_name(tuple(average_color))

    # shutil.rmtree('./images')
    return closest_name
