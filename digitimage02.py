# 이미지 여러개 출력하기

import sklearn.datasets
import matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

for idx in range(50):
    plt.subplot(5, 10, idx + 1)
    plt.axis("off")
    plt.title(digits.target[idx])
    plt.imshow(digits.images[idx], cmap='Greys')

plt.show()