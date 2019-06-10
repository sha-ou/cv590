#!/usr/bin/python3

###################################################################
#    File name     : cv590.py
#    Author        : sha-ou
#    Date          : Wed 29 May 2019 11:00:36 CST
#    Description   :
###################################################################

import pandas as pd
import matplotlib.pyplot as plt


def txt2csv(txtf):
    content = ''
    fname = str(txtf).split('.')[0]
    csvf = fname + '.csv'

    txtfp = open(txtf, 'r')
    content = txtfp.read()
    txtfp.close()

    csvfp = open(csvf, 'w')
    csvfp.write(content.replace('\t', ','))
    csvfp.close()

    return


class CV590Class():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
