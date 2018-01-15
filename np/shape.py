import numpy as np

# np.shape 获取数组的维度信息
template = "%s.shape() = %s"
a = [1, 2, 3, 4]
print(template % (a, np.shape(a)))

b = [[1, 2], [3, 4], [5, 6]]
print(template % (b, np.shape(b)))

b = [[[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]]
print(template % (b, np.shape(b)))

data = [(12, 12), (21, 14), (19, 15), (23, 26), (25, 10), (20, 14), (13, 10), (12, 13), (19, 26), (17, 11), (13, 11), (13, 12), (5, 17), (5, 17), (15, 13), (18, 18), (5, 12), (15, 8), (9, 12), (9, 12)]
print(template % (data, np.shape(data)))

n, m = np.shape(data)

print(n,m)

maxes = np.amax(data, axis=0)
mins = np.amin(data, axis=0)

print(maxes)
print(mins)