

def checkNumbers(nums):
    for num in nums:
        if int(num) <= 0 or int(num) >13:
            print('无效数字: %s . 请输入1-13之内的数字' % num)
            return False

    return True


def getNumbers(expectedNumberCount):
    nums = []
    while True:

        print('=========== 游戏开始。 请输入四个数字（空格或逗号分隔）: ')
        inStr = input()
        #print('got numbers: %s' % inStr)

        numStrs = inStr.split()
        if len(numStrs) == expectedNumberCount:
            break

        numStrs = inStr.split(',')
        if len(numStrs) == expectedNumberCount:
            break

    for num in numStrs:
        if num == 'J' or num == 'j':
            num = 11
        if num == 'Q' or num == 'q':
            num = 12
        if num == 'K' or num == 'k':
            num = 13

        nums.append(int(num))
    return nums


def opLevel(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op is None:
        return 3
    else:
        return 0


def compOp(op, prevOp):

    op1Level = opLevel(op)
    op2Level = opLevel(prevOp)
    return op1Level - op2Level


answerMap = {}
def showAnswer(stack):

    # 避免重复输出
    global answerMap
    keyStr = repr(stack)
    if answerMap.__contains__(keyStr):
        answerMap[keyStr] = answerMap[keyStr] + 1
        return
    else:
        answerMap[keyStr] = 1

    # for symbol in stack:
    #     print('%s ' % symbol)
    # reversedStack = stack[:]
    # reversedStack.reverse()
    # print('found answer reversedStack is: ' + repr(reversedStack))

    # A1 x1 A2 x2 A3 x3 A4
    # 从右向左构造算式

    # 初始算式 A4  prev算符为None， 优先级最高，不用加括号
    # 循环， 直到stack为空
    #   取 x[n-i] 和 a[n-i]， 比较算符优先级，
    #   x[n-i] 与 prev算符 进行比较，
    #     运算级比prev低， 不加括号
    #     运算级相同 且为 *或+，不加括号，
    #                     /或-，不加括号
    #     运算级比prev高， 需要加括号
    #   prev = x[n-i]
    #   输出 a[n-i] x[n-i] currentExpr

    stackLen = len(stack)
    i = stackLen - 1
    prevExpr = stack[i]
    prevOp = None
    i = i - 1
    while i>=0:
        op = stack[i]
        a = stack[i-1]

        compResult = compOp(op, prevOp)
        if compResult < 0:
            # 不加括号
            pass
        elif compResult == 0:
            if op == '-' or op == '/':
                # 不加括号
                pass
            else:
                # 不加括号
                pass
        elif compResult > 0:
            # 加括号
            prevExpr = '(%s)' % prevExpr

        # 输出算式
        prevOp = op
        prevExpr = '%s %s %s' % (prevExpr, op, a)

        i = i - 2

    print('    答案: ' + prevExpr)

stack = []
def calc(targetPoint, nums):
    global stack

    # 出口条件
    numLen = len(nums)
    if numLen == 1:
        n = nums[0]
        if targetPoint == n:
            stack.append(str(n))
            # 计算完成。 输出答案
            showAnswer(stack)
            stack.pop()
        else:
            return False

    # 取出一个数n
    for i in range(0, numLen):
        n = nums[i]
        remainNums = []
        remainNums = nums[:]
        remainNums.pop(i)

        stack.append(str(n))
        for method in [ '+', '-', '*', '/' ]:
            # 尝试加减乘除计算m
            if method == '+':
                m = targetPoint - n
                if m > 0:
                    stack.append(method)
                    calc(m, remainNums)
                    stack.pop()

            if method == '-':
                m = targetPoint + n
                stack.append(method)
                calc(m, remainNums)
                stack.pop()

            if method == '*':
                m = targetPoint / n
                if m == int(m):
                    stack.append(method)
                    calc(m, remainNums)
                    stack.pop()

            if method == '/':
                m = targetPoint * n
                stack.append(method)
                calc(m, remainNums)
                stack.pop()



        stack.pop()


def main():
    print('main start')
    TARGET_POINT = 24
    NUMBER_COUNT = 4
    try:
        while True:
            nums = []
            # nums = [1, 1, 4, 6]
            # nums = [8, 6, 3, 3]

            if len(nums) == 0:
                nums = getNumbers(NUMBER_COUNT)
                if not checkNumbers(nums):
                    return

                # print('nums: ')
                # print(nums)

            calc(TARGET_POINT, nums)
    except KeyboardInterrupt as e:
        print('stop')

    print('main stop')



if __name__ == '__main__':
    main()
