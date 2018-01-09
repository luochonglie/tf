import scipy
from matplotlib import pyplot

DataRange = range(0, 360)
DataRange = list(map(scipy.deg2rad, DataRange))
Data1 = list(map(scipy.sin, DataRange))
Data2 = list(map(scipy.cos, DataRange))

toggle = True


def onclick(event):
    global toggle

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
