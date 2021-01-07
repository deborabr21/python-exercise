#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests


def main():
    """Run time code"""
    # create r, which is our request object
    astros = requests.get("http://api.open-notify.org/astros.json").json()

    print("People in space: ", astros["number"])

    for x in astros["people"]:
        print(f"{x['name']} on the {x['craft']}")


main()
