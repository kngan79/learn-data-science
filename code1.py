import random

def Name(index):
    row = arr[index]
    splited = row.split(',')
    return splited[4]

f=open("iris.data", "r")
contents =f.read()
arr = contents.split('\n')
random.shuffle(arr)

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

train = []
train.extend(setosa[0:setosa80])
train.extend(versicolor[0:versicolor80])
train.extend(virginica[0:virginica80])

train_s = "" 
for i in range(len(train)):
    train_s += train[i] + '\n'
print (train_s)

f=open("train.data","w")
f.write(train_s)
f.close()

test = []
test.extend(setosa[setosa80:len(setosa)])
test.extend(versicolor[versicolor80:len(versicolor)])
test.extend(virginica[virginica80:len(virginica)])

test_s = "" 
for i in range(len(test)):
    test_s += test[i] + '\n'
print (test_s)

f=open("test.data","w")
f.write(test_s)
f.close()



