import sklearn.datasets
import  matplotlib.pyplot as plt

digits = sklearn.datasets.load_digits()

print(digits.images[1000])

plt.imshow(digits.images[1000], cmap='Greys')
plt.show()