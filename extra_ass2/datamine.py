from pomegranate import *
import math
import cairo
import json
import os
from pprint import pprint


def load_data():
    """Load data element-data from json-files inside websites-folder"""

    # array that will contain all the elements from the json-files
    data = []

    # keys that will be left to the element data
    wanted_keys = ["feature", "xPosition", "yPosition", "width", "height"]

    for filename in os.listdir('websites'):
        with open('websites/' + filename) as json_data:
            website_data = json.load(json_data)
            data.append(website_data)

    return data


def normalize_data(data):
    """
    Normalize given data such that element locations and sizes are given as a
    float between 0 and 1 describing the relative size compared to the element's
    root element.
    """

    normalized_data = []

    for website in data:
        elements = website["elements"]
        # all the root element's are actually same sized so this is kind of unnecessary
        root_height = elements["0"]["height"]
        root_width = elements["0"]["width"]

        for el_ind in elements:
            el = elements[el_ind]
            n_xpos = 1.0 * el["xPosition"] / root_width
            n_ypos = 1.0 * el["yPosition"] / root_height
            n_width = 1.0 * el["width"] / root_width
            n_height = 1.0 * el["height"] / root_height

            el["xPosition"] = n_xpos
            el["yPosition"] = n_ypos
            el["width"] = n_width
            el["height"] = n_height

            elements[el_ind] = el

        website["elements"] = elements
        normalized_data.append(website)

    return normalized_data


def main():
    """Main program logic"""

    data = load_data()
    n_data = normalize_data(data)
    pprint(n_data)


if __name__ == '__main__':
    main()
