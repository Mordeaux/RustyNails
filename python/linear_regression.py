from config import rusty_nails


class LinearRegression(object):
    """This class should contain methods that allow the user to
    configure and process a linear regression algorithm."""

    def __init__(self):
        self.result = None

    def process(self):
        self.result = rusty_nails.linear_regression(100)

    def display_results(self):
        """This method will be used to display the results of a linear
        regression in some kind of cool way, like a graph or something.
        """
        if self.result:
            print self.result


if __name__ == '__main__':
    linear_regression = LinearRegression()
    linear_regression.process()
    linear_regression.display_results()
