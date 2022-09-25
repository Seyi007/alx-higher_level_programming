#!/usr/bin/python3
""" script that takes 2 arguments
to list github repo and owner name """


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))
    if r.status_code >= 400:
        print('None')
    else:
        for per in r.json()[:10]:
            print("{}: {}".format(per.get('sha'),
                                  per.get('commit').get('author').get('name')))
