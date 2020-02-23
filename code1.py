from random import randint

f=open("iris.data", "r")
contents =f.read()
# print(contents)
arr = contents.split('\n')

def Name(index):
    row = arr[index]
    splited = row.split(',')
    return splited[4]
setosa = []
versicolor =[]
virginica = []
for i in range(len(arr)):
    if Name(i)=="Iris-setosa":
        setosa.append(arr[i])
    if Name(i)=="Iris-versicolor":
        versicolor.append(arr[i])
    if Name(i)=="Iris-virginica":
        virginica.append(arr[i])

setosa80 = len(setosa) * 80 // 100
versicolor80 = len(versicolor) * 80 // 100
virginica80 = len(virginica) * 80 // 100

a = []
a.extend(setosa[0:setosa80])
a.extend(versicolor[0:versicolor80])
a.extend(virginica[0:virginica80])
