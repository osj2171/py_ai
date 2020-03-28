import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import sklearn.datasets
import sklearn.svm
import numpy

# 이미지 파일을 수치 리스트로 전환
def imageToData(filename):
    greyImage = PIL.Image.open(filename).convert("L")
    greyImage = greyImage.resize((8,8), PIL.Image.ANTIALIAS)

    dispImage = PIL.ImageTk.PhotoImage(greyImage.resize((300,300)))
    imageLabel.configure(image=dispImage)
    imageLabel.image = dispImage

    # 수치 리스트 전환
    numImage = numpy.asarray(greyImage, dtype=float)
    numImage = numpy.floor(10-10*(numImage/256))
    numImage = numImage.flatten()
    return numImage

def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    #예측결과 표시
    n = clf.predict([data])
    textLabel.configure(text="이 그림은 %d입니다!" % n)


def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        print("파일경로", fpath)
        data = imageToData(fpath)
        print(data)
        predictDigits(data)

root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root, text="파일 열기", command=openFile)
imageLabel = tk.Label()
textLabel = tk.Label()

btn.pack()
imageLabel.pack()
textLabel.pack()

tk.mainloop()