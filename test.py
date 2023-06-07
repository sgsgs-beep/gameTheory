import numpy as np

arrays = np.empty((0, 3, 512, 512)) #创建空数组

for i in range(100):
    image = np.ones(shape=(3, 512, 512)) #使用image模拟一张3通道，512×512的图片
    data = image.reshape((1, 3, 512, 512))
    arrays = np.concatenate((arrays, data), axis=0)

print(np.shape(arrays))
print(type(arrays))
