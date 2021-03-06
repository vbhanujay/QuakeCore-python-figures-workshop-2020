import numpy as np
import matplotlib.pyplot as plt
import all_paths as ap
import engformat as ef


def create():

    data = np.loadtxt(ap.MODULE_DATA_PATH + 'basic_raw_data.csv', skiprows=1, delimiter=',').T
    x = data[0]
    y = data[1]
    ps = np.polyfit(x, y, deg=2)
    y_fit = ps[0] * x ** 2 + ps[1] * x + ps[2]
    bf, subplot = plt.subplots()
    for i in range(len(x)):
        subplot.plot(x[i], y[i], 'o', c='b', alpha=0.5, label='Raw data')
    subplot.plot(x, y_fit, c='r', label='Fitted')
    subplot.axvspan(0.5, 1.5, color='orange', alpha=1)
    cline = ef.create_custom_legend_patch(label='Critical zone', c='orange', alpha=0.3)
    ef.revamp_legend(subplot, loc='upper left', add_handles=[cline])
    plt.show()


if __name__ == '__main__':
    create()
