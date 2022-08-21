from DEVS import DEVS
# from vniversvs import VNIVERSVS

devs = DEVS()
devs.fiat()
# devs.env = input('what env? ')
devs.env = 'd'
vniversvs = devs.vniversvs
tester = devs.tester
davar = devs.davar

# if devs.window_flag:
#     import pygame
#     from PyQt5 import QtCore, QtGui, QtWidgets
#     window = devs.window









def main():

    ###
    ###
    ###
    ###

    tester.run()

    devs.run_davar()

    pass

if __name__ == '__main__':
    main()
