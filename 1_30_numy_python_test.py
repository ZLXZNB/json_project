import numpy as np

# a = [1, 2, 3, 4, 5, 6]
# print(a[:, 0::2])
position = 3
d_model = 20
i = np.arange(d_model)[np.newaxis, :]
print(i)
print(i // 2)
print(2 * (i // 2))
print(np.float32(d_model))
print((2 * (i // 2)) / np.float32(d_model))
d = (2 * (i // 2)) / np.float32(d_model)
print(np.power(10000, d))
print(1 / np.power(10000, d))
m = 1 / np.power(10000, d)
print(m.shape)

f = np.arange(position)[:, np.newaxis]
print("f")
print(f)
print(f.shape)

print(m * f)
print((m*f).shape)