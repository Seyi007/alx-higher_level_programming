#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        js = r.json()
        if js == {}:
            print('No result')
        else:
            print('[{}] {}'.format(js.get('id'), js.get('name')))
    except ValueError:
        print('Not a valid JSON')
