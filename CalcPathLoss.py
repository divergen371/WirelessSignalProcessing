import numpy as np
import scipy
import matplotlib.pyplot as plt

SPEED_OF_LIGHT = 299792458.0


def CalcPathLoss(freq: float, d: float) -> float:
    _lambda = SPEED_OF_LIGHT / freq
    loss = (4.0 * np.pi * d / _lambda) ** 2
    return loss


def PlotPathLoss(freq: float, dist: float, loss: float) -> None:
    plt.figure()
    ax = plt.gca()
    title = "Distance attenuation at %dHz" % (freq)
    plt.title(title)
    ax.axes.xaxis.set_visible(True)
    ax.axes.yaxis.set_visible(True)

    plt.grid(True)
    plt.xlabel("distance(m)")
    plt.ylabel("pathloss(dB)")
    plt.grid = True
    plt.plot(dist, loss, drawstyle="steps-post")
    plt.show()


if __name__ == "__main__":
    print("Freequency:", end="")
    freq = float(input())
    print("Max Distance(m):", end="")
    dist = float(input())
    d = np.arange(dist / 1000.0, dist, dist / 1000.0)
    loss = CalcPathLoss(freq, d)
    loss_db = -10.0 * np.log10(loss)
    PlotPathLoss(freq, d, loss_db)
