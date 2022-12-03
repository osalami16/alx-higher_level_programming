#!/usr/bin/python3
f __name__ == "__main__":
    import hidden_4

    for attr in dir(hidden_4):
        if attr.startswith("__"):
            continue
        print("{}".format(attr))
