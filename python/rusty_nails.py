from config import rusty_nails


def threaded_incrementor():
    rusty_nails.process()
    print("Python is done!")


if __name__ == '__main__':
    threaded_incrementor()
