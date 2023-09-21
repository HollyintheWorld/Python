import random
MAX_Y_SIZE = 32
MAX_Z_SIZE = 32


class Cube:
    def __init__(self):
        self.xList = []
        self.xSize = 0


class Y:
    def __init__(self, data, isFromList=False):
        # z를 반으로 자를 때
        if isFromList:
            self.zList = data
            self.zSize = len(data)
            # 해당 줄의 가장 낮은 숫자
            self.lowest = data[0]
        # 첫 줄을 만들 때
        else:
            self.zList = [data]
            self.zSize = 1
            # 해당 줄의 가장 낮은 숫자
            self.lowest = data


class X:
    def __init__(self, data, isFromList=False):
        # y를 반으로 자를 때
        if isFromList:
            self.yList = data
            self.ySize = len(data)
            # 해당 면의 가장 낮은 숫자
            self.lowest = data[0].lowest
        # 첫 면을 만들 때
        else:
            self.yList = [Y(data)]
            self.ySize = 1
            # 해당 면의 가장 낮은 숫자
            self.lowest = data


def splitZ(targetX, targetYIndex):
    targetY1 = targetX.yList[targetYIndex]
    targetY2 = Y(targetY1.zList[MAX_Z_SIZE // 2:], True)
    targetY1.zList = targetY1.zList[:MAX_Z_SIZE // 2]
    targetY1.zSize = MAX_Z_SIZE // 2
    targetX.yList.insert(targetYIndex + 1, targetY2)
    targetX.ySize += 1


def splitY(targetCube, targetXIndex):
    targetX1 = targetCube.xList[targetXIndex]
    targetX2 = X(targetX1.yList[MAX_Y_SIZE // 2:], True)
    targetX1.yList = targetX1.yList[:MAX_Y_SIZE // 2]
    targetX1.ySize = MAX_Y_SIZE // 2
    targetCube.xList.insert(targetXIndex + 1, targetX2)
    targetCube.xSize += 1


def insert(targetCube, data):
    # if cube is empty
    if targetCube.xSize == 0:
        targetCube.xList.append(X(data))
        targetCube.xSize += 1
        return
    # find the position of x
    currentXIndex = targetCube.xSize - 1
    mid = currentXIndex // 2
    while mid > 0:
        if (targetCube.xList[currentXIndex - mid].lowest >= data):
            currentXIndex -= mid
        mid //= 2
    while (currentXIndex > 0 and targetCube.xList[currentXIndex].lowest >= data):
        currentXIndex -= 1
    currentX = targetCube.xList[currentXIndex]
    # Found proper position for x
    # find the position of y
    currentYIndex = currentX.ySize - 1
    mid = currentYIndex // 2
    while mid > 0:
        if (currentX.yList[currentYIndex - mid].lowest >= data):
            currentYIndex -= mid
        mid //= 2
    while (currentYIndex > 0 and currentX.yList[currentYIndex].lowest >= data):
        currentYIndex -= 1
    currentY = currentX.yList[currentYIndex]
    # Found proper position for y
    # find the position of z
    currentZIndex = currentY.zSize - 1
    mid = currentZIndex // 2
    while mid > 0:
        if (currentY.zList[currentZIndex - mid] >= data):
            currentZIndex -= mid
        mid //= 2
    while (currentZIndex > 0 and currentY.zList[currentZIndex] >= data):
        currentZIndex -= 1
    # Found proper position for z
    # insert the item to proper position
    if (currentY.zList[currentZIndex] >= data):
        currentY.zList.insert(currentZIndex, data)
    else:
        currentY.zList.insert(currentZIndex + 1, data)
    currentY.zSize += 1
    if currentZIndex == 0:
        currentY.lowest = currentY.zList[0]
        if currentYIndex == 0:
            currentX.lowest = currentY.zList[0]
    # if size reached max, split them
    if currentY.zSize == MAX_Z_SIZE:
        splitZ(currentX, currentYIndex)
        if currentX.ySize == MAX_Y_SIZE:
            splitY(targetCube, currentXIndex)
    # print_cube(targetCube)


def print_cube(targetCube):
    if targetCube.xSize == 0:
        return
    for i in targetCube.xList:
        for j in i.yList:
            for k in j.zList:
                print(k, end=' ')
            # print("")
        # print("")
    print("")


def make_array(targetCube):
    if targetCube.xSize == 0:
        return []
    retval = []
    for i in targetCube.xList:
        for j in i.yList:
            retval += j.zList
    return retval


def isSorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))


cube = Cube()
for i in range(500):
    insert(cube, random.randint(1, 100))
print_cube(cube)
print(isSorted(make_array(cube)))

