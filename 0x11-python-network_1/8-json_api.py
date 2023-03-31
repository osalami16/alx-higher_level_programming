#!/usr/bin/python3
"""
Python scritp that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q.
If no argument is given, set q="".
If the response body is properly JSON formatted and not empty, display the
id and name like this: [<id>] <name>, otherwise: Display Not a valid JSON.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    response = requests.post(url, data=payload)
    try:
        json_output = response.json()
        if not json_output:
            print("No result")
        else:
            my_id = json_output.get('id')
            my_name = json_output.get('name')
            print("[{}] {}".format(my_id, my_name))
    except ValueError as invalid_json:
        print("Not a valid JSON")
