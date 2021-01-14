#!/usr/bin/python3

import requests


def main():
    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key"
                             "=nndIcVrONfE10xZZSlLBIq6f0BcOnbcEFFkYKl20").json()

    # print(roverresp)

    # Return every link to a Mars Rover photo in this API.
    for every_dict in roverresp["photos"]:
        print("Images: ", every_dict["img_src"])

    # Return every link to a Mars Rover photo in this API ALONG WITH the name of the Rover that took it and the date it
    # was taken.
    for every_dict in roverresp["photos"]:
        print()
        print("Rover: ", every_dict["rover"]["name"])
        print("Date: ", every_dict["earth_date"])
        print("Images: ", every_dict["img_src"])


if __name__ == "__main__":
    main()
