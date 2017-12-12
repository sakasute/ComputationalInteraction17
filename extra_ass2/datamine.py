from pomegranate import *
import math
import cairo
import json
import os


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
            # for el_ind in website_data["elements"]:
            #     el_data = website_data["elements"][el_ind]
            #     el_data_pruned = {key: el_data[key] for key in wanted_keys}
            #     data.append(el_data_pruned)

    return data


def normalize_data(data):
    """
    Normalize given data such that element locations and sizes are given as a 
    float between 0 and 1 describing the relative size compared to the element's
    root element.
    """


def main():
    """Main program logic"""

    data = load_data()
    print(data[0])


if __name__ == '__main__':
    main()
