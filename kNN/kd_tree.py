#!/usr/bin/python3

from operator import itemgetter

class Node:
    def __init__(self, _sa, _loc, _lc, _rc, _p):
        self.splitAttribute = _sa
        self.location = _loc
        self.left_child = _lc
        self.right_child = _rc
        self.parent = _p
        return


def isLeft(self):
    if self.parent.left_child == self:
        return True
    else:
        return False


def isRight(self):
    if self.parent.right_child == self:
        return True
    else:
        return False


def isRoot(self):
    if self.parent == None:
        return True
    else:
        return False


def neghbor(self):
    if self.isRight() == True:
        return self.parent.left_child
    elif self.isLeft() == True:
        return self.parent.right_child
    else:
        return None


def KDTree(point_list, pre_axis=0):
    try:
        k = len(point_list[0])
    except IndexError as e:
        return None
    axis = pre_axis % k

    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2
    _left_child = KDTree(point_list[:median], pre_axis + 1)
    _right_child = KDTree(point_list[median + 1:], pre_axis + 1)
    node = Node(axis, point_list[median], _left_child, _right_child, None)
    if node.left_child != None:
        node.left_child.parent = node;
    if node.right_child != None:
        node.right_child.parent = node
    return node


def distancePoint(pointA, pointB):
    if len(pointA) != len(pointB):
        return -1
    d = len(pointA)
    count = 0
    for i in range(d):
        count += (pointA[i] - pointB[i]) ** 2
    return count ** 0.5


def searchKDTree(root, point, k=1):
    if len(root.location) != len(point):
        return None
    axis = root.splitAttribute
    value = point[axis];
    nodeT = root
    while nodeT != None:
        if value <= root.location[axis]:
            root = nodeT
            nodeT = root.left_child
        else:
            root = nodeT
            nodeT = root.right_child
    # back
    curPoint = root;
    curDis = distancePoint(curPoint.location, point)
    nodeT = root;
    while root.isRoot() != True:
        if root.neghbor() != None:
            dis = distancePoint(point, root.neghbor().location)
            if dis < curDis:
                curPoint = root.neghbor()
                curDis = dis
        if root.isRoot() != True:
            dis = distancePoint(point, root.parent.location)
            if dis < curDis:
                curPoint = root.parent
                curDis = dis
        root = root.parent
    return curPoint

def main():
    """Example usage"""
    point_list = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    tree = KDTree(point_list)
    test_point = (4, 7);
    node = searchKDTree(tree, test_point)
    print(tree.location)

if __name__ == '__main__':
    main()
