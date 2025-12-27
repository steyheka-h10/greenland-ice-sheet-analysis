#!/usr/bin/env python3
"""
Process melt extent data for Greenland ice sheet analysis.
Currently supports 2017 melt season data.
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_melt_data(filepath):
    """Load melt extent CSV file."""
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    return df

def plot_melt_extent(df, year):
    """Plot melt extent over time."""
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['melt_extent_km2'])
    plt.title(f'Greenland Ice Sheet Melt Extent ({year})')
    plt.xlabel('Date')
    plt.ylabel('Melt Extent (km²)')
    plt.grid(True)
    plt.savefig(f'melt_extent_{year}.png')
    plt.show()

if __name__ == '__main__':
    # Example usage for 2017 data
    data_2017 = load_melt_data('../data/2017_melt_extent.csv')
    print(f"Loaded {len(data_2017)} records for 2017")
    plot_melt_extent(data_2017, 2017)