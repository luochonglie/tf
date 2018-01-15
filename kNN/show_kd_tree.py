import kd_tree_idx

point_list = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
tree = kd_tree_idx.KDTree(point_list)
print(tree.location)
