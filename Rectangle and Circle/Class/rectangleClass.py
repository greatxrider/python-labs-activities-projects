# Jeph Mari Daligdig
# Rectangle Class

import matplotlib.pyplot as plt


class Rectangle(object):
    # Constructor
    def __init__(self, width, height, color="r"):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self):
        plt.gca().add_patch(
            plt.Rectangle((0, 0), self.width, self.height, fc=self.color)
        )
        plt.axis("scaled")
        plt.show()
