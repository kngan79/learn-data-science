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

a = setosa[0:setosa80]
a.append(versicolor[0:versicolor80])
a.append(virginica[0:virginica80])

print(a[-1])

s = ""
for i in range(len(a)):
    # print(type(a[i]))
    s = s  + "a"
    if i != len(a)-1:
        s = s  + '\n'

# print(s)