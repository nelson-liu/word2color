# import the necessary packages
from sklearn.cluster import KMeans
import argparse
import cv2

def get_average_colors(img_array):
	if len(img_array) == 0 or img_array is None:
		return [0, 0, 0]
		
	avg_colors_list = []
	sum_colors = [0.0, 0.0, 0.0]
	for image in img_array:
		dominant_color, cluster = get_dominant_color(image)
		avg_colors_list.append(dominant_color)

	for color in avg_colors_list:
		sum_colors[0] += color[0]
		sum_colors[1] += color[1]
		sum_colors[2] += color[2]

	num_colors = float(len(avg_colors_list))
	avg_color = map(lambda x: int(x / num_colors), sum_colors)
	return avg_color

def get_dominant_color(image_path):
	image = cv2.imread(image_path)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# reshape the image to be a list of pixels
	image = image.reshape((image.shape[0] * image.shape[1], 3))

	# cluster the pixel intensities
	clt = KMeans(n_clusters = 1)
	clt.fit(image)

	dominant_color = clt.cluster_centers_[0]

	# show our color bart
	return (dominant_color, clt)
