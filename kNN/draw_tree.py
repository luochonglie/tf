import matplotlib_tree as mt
import numpy as np

from kNN import kdtree

axis_name = ["x", "y"]


def createTreeInfo(node):
    # return {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}

    if node.is_leaf:
        return "%s (%d, %d)" % (axis_name[node.axis], node.data[0], node.data[1])

    left_dic = None
    if node.left.data is not None:
        left_dic = createTreeInfo(node.left)

    right_dic = None
    if node.right.data is not None:
        right_dic = createTreeInfo(node.right)

    dic = {"%s (%d, %d)" % (axis_name[node.axis], node.data[0], node.data[1]): {}}

    if left_dic is not None:
        dic["%s (%d, %d)" % (axis_name[node.axis], node.data[0], node.data[1])][" "] = left_dic

    if right_dic is not None:
        dic["%s (%d, %d)" % (axis_name[node.axis], node.data[0], node.data[1])]["  "] = right_dic

    return dic


def draw_tree(in_tree):
    info = createTreeInfo(in_tree)
    print(info)
    mt.create_plot(info)


if __name__ == '__main__':
    points = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]])
    # points = np.random.randint(10, 100, size=[30, 2])
    root = kdtree.create(np.ndarray.tolist(points))
    draw_tree(root)
