# imports always go at the top of your code
import requests


def main():
    """Run time code"""
    # create r, which is our request object
    recipe = requests.get("http://www.recipepuppy.com/api/").json()

    print("The version number is: ", recipe["version"])

    for x in recipe["results"]:
        print(f"{x['title']}")
        print(f"{x['ingredients']}")

main()
