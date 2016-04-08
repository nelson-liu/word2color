from bs4 import BeautifulSoup
import cv2
from IPython.utils.path import ensure_dir_exists
import numpy as np
import os
import re
import requests
import urllib2

class BingScraper():
    def get_soup(self, url):
        return BeautifulSoup(requests.get(url).text, "html.parser")
    # end def

    def download_images(self, color, num_images):
        if num_images > 19:
            raise ValueError('Number of images to download '
                             'must be less than 20.')
        query = color + ' color'
        url = 'http://www.bing.com/images/search?q=' + query
        soup = self.get_soup(url)
        images = [a['src']
                  for a in soup.find_all('img',
                                         {'src': re.compile('mm.bing.net')})]
        images = images[:num_images]
        download_directory = 'images/' + color
        ensure_dir_exists(download_directory)
        for img in images:
            raw_img = urllib2.urlopen(img).read()
            image = np.asarray(bytearray(raw_img), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)

            x_size, y_size, _ = image.shape
            cropped_image = image[0:y_size, int(x_size*.18):int(x_size*1.18)]

            cntr = len([i for i in os.listdir(download_directory)
                        if color in i]) + 1
            filename = ("images/" + color + '/' + color +
                        "_" + str(cntr) + '.jpg')
            cv2.imwrite(filename, cropped_image)
        # end for
    # end def
# end class
