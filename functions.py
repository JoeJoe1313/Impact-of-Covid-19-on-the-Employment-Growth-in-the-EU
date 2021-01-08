import csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def multiple_plots(original_data, fits=None, forecasts=None, colours=None, labels=None):
    _, ax = plt.subplots(1, 1, figsize=(10, 3))
    ax.plot(original_data, color='black', marker='o', label='Original data')
    if None not in [fits, colours, labels]:
        if forecasts is None:
            forecasts = [None] * len(fits)
        assert len(fits) == len(forecasts)
        assert len(fits) == len(colours)
        assert len(fits) == len(labels)
        for fit, forecast, colour, label in zip(fits, forecasts, colours, labels):
            ax.plot(fit, color=colour, linestyle='--', label=label)
            if forecast is not None:
                ax.plot(forecast, color=colour, linestyle='--', marker='o')
    ax.set_ylim(ymin=0)
    ax.legend()
    plt.show()
