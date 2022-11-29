# define mis function

import pandas as pd

def color_positive_green(df, mask):
    ret = pd.DataFrame('', index=df.index, columns=df.columns)

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if mask[i,j] != 0:
                if i % 2 == 0:
                    ret.iloc[i,j] = 'background-color: lime'
                else:
                    ret.iloc[i,j] = 'background-color: yellow'

    return ret


def color_positive_green_vertical(df):
    ret = pd.DataFrame('', index=df.index, columns=df.columns)

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if i % 2 == 0:
                ret.iloc[i,j] = 'background-color: lime'
            else:
                ret.iloc[i,j] = 'background-color: yellow'

    return ret


def color_positive_green_horizontal(df):
    ret = pd.DataFrame('', index=df.index, columns=df.columns)

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if j % 2 == 0:
                ret.iloc[i,j] = 'background-color: lime'
            else:
                ret.iloc[i,j] = 'background-color: yellow'

    return ret
