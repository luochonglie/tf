import scipy_lib
from matplotlib import pyplot

DataRange = range(0, 360)
DataRange = list(map(scipy_lib.deg2rad, DataRange))
Data1 = list(map(scipy_lib.sin, DataRange))
Data2 = list(map(scipy_lib.cos, DataRange))

level = True


def onclick(event):
    global level

    toggle = not toggle
    event.canvas.figure.clear()

    if toggle:
        event.canvas.figure.gca().plot(Data1)
    else:
        event.canvas.figure.gca().plot(Data2)

    event.canvas.draw()


fig = pyplot.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

pyplot.plot(Data1)
pyplot.show()
