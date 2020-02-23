def get_file(fileName):
    file = open(fileName, "r")
    content = file.read()
    rows = content.split('\n')
    # fix newline of row
    while rows[-1] == "": rows.pop()
    return rows

def get_attributes(row):
    attributes = row.split(',')
    attributes.pop()
    for i in range(len(attributes)):
        attributes[i] = float(attributes[i])
    return attributes

def get_name(row):
    attributes = row.split(',')
    return attributes[4]

# Range will be from -1 to 1
def min_max_normalization(min_element, max_element, current_value):
    return (current_value - min_element + 0.0) / (max_element - min_element + 0.0) * 2 - 1

def sqr(x):
    return x*x

# L2 distance
def get_distance(row_1, row_2, min_attrs, max_attrs):
    a = get_attributes(row_1)
    b = get_attributes(row_2)
    dist = 0.0
    for i in range(len(a)):
        a[i] = min_max_normalization(min_attrs[i], max_attrs[i], a[i])
        b[i] = min_max_normalization(min_attrs[i], max_attrs[i], b[i])
        dist += sqr(a[i] - b[i])
    return dist

def get_min_attributes(train_set):
    # A very large number
    oo = 1000000.0
    min_attributes = [oo, oo, oo, oo]
    for row in train_set:
        current_attribute = get_attributes(row)
        for i in range(4):
            min_attributes[i] = min(min_attributes[i], current_attribute[i])
    return min_attributes

def get_max_attributes(train_set):
    # A very large number
    max_attributes = [0.0, 0.0, 0.0, 0.0]
    for row in train_set:
        current_attribute = get_attributes(row)
        for i in range(4):
            max_attributes[i] = max(max_attributes[i], current_attribute[i])
    return max_attributes

def take_first_element(elem):
    return elem[0]

# Use K-nearest neighbor
def classify_object(row_test, train_set, min_attrs, max_attrs, k = 10):
    # Holds distance with name of object
    distance_array = []
    for row_train in train_set:
        distance = get_distance(row_test, row_train, min_attrs, max_attrs)
        distance_array.append((distance, get_name(row_train)))
    distance_array = sorted(distance_array, key=take_first_element)[:k]

    cnt = {
        "Iris-setosa": 0,
        "Iris-versicolor": 0,
        "Iris-virginica": 0
    }
    name = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    for val in distance_array:
        cnt[val[1]] += 1

    if cnt["Iris-setosa"] >= cnt["Iris-versicolor"] and cnt["Iris-setosa"] >= cnt["Iris-virginica"]:
        return "Iris-setosa"
    if cnt["Iris-versicolor"] >= cnt["Iris-setosa"] and cnt["Iris-versicolor"] >= cnt["Iris-virginica"]:
        return "Iris-versicolor"
    if cnt["Iris-virginica"] >= cnt["Iris-versicolor"] and cnt["Iris-virginica"] >= cnt["Iris-setosa"]:
        return "Iris-virginica"

train = get_file("train.data")
test = get_file("test.data")

min_attrs = get_min_attributes(train)
max_attrs = get_max_attributes(train)

for val in test:
    obj = classify_object(val, train, min_attrs, max_attrs)
    print(obj, get_name(val))