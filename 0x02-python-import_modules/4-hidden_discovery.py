
#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    items = dir()
    for i in range(0, len(items)):
        if items[i][0:2] != "__":
            print("{}".format(items[i]))
