# 학습 이미지 불러오기


import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("데이터의 개수:", len(digits.images))
print("이미지 데이터---------------------")
print(digits.images[0])
print("무슨 데이터:", digits.target[0])
