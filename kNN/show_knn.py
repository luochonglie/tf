#!/usr/bin/python
# -*-coding:utf-8 -*-


from sklearn import neighbors
import numpy as np
import matplotlib.pyplot as plt


def draw_training_points(figure):
    figure.clear()
    plt.title('k-NN (k = ' + str(k) + ')')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    figure.gca().scatter(x1, y1, c='b', marker='s', s=50, alpha=0.8, label="class 1")
    figure.gca().scatter(x2, y2, c='r', marker='^', s=50, alpha=0.8, label="class 2")
    plt.legend()


def draw_testing_point(figure):
    plt.title('k-NN (k = ' + str(k) + ')'
              + '\np = (' + str(x3[0]) + ', ' + str(y3[0]) + ')')
    figure.gca().scatter(x3, y3, c='g', s=50, alpha=0.8)


def draw_nearests(figure):
    print("testing_point", testing_point)
    title = 'k-NN (k = ' + str(k) + ')'

    prediction = clf.predict(testing_point)
    title += '\np = (' + str(x3[0]) + ', ' + str(y3[0]) + '), class = ' + str(prediction[0])

    nn = clf.kneighbors(testing_point, k, False)
    title += '\nNN = ['
    for i in nn[0]:
        title += str(training_points[i]) + ", "
    title += "]"
    figure.gca().scatter(x_val[nn[0]], y_val[nn[0]], c='g', s=150, alpha=0.3)

    plt.title(title)


def draw_step_0(figure):
    draw_training_points(figure)


def draw_step_1(figure):
    draw_testing_point(figure)
    draw_nearests(figure)


# def draw_step_2(figure):



def onclick(event):
    global toggle

    toggle = (toggle + 1) % 2

    if toggle == 1:
        global x3
        global y3
        global testing_point
        x3 = [round(event.xdata, 2)]
        y3 = [round(event.ydata, 2)]
        testing_point = list(zip(x3, y3))

    eval('draw_step_' + str(toggle))(event.canvas.figure)
    event.canvas.draw()


# 随机生成 6 组 200 个的正态分布
class1_count = 100
class2_count = 100
k = 5

x1 = np.random.randint(10, 300, class1_count)
y1 = np.random.randint(10, 300, class1_count)

x2 = np.random.randint(50, 200, class2_count)
y2 = np.random.randint(50, 200, class2_count)

x_val = np.concatenate((x1, x2))
y_val = np.concatenate((y1, y2))

training_points = list(zip(x_val, y_val))
print(training_points)

labels = [1] * class1_count + [2] * class2_count

clf = neighbors.KNeighborsClassifier(k)
clf.fit(training_points, labels)

x3 = [30]
y3 = [30]
testing_point = list(zip(x3, y3))
print(testing_point)

toggle = 0

fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', onclick)

draw_step_0(fig)

plt.show()
input()
