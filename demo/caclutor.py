import sys
import math


def calc(term):
    # 替换符号
    term = term.replace(' ', '')
    term = term.replace('^', '**')
    term = term.replace('=', '')
    term = term.replace('?', '')
    term = term.replace('%', '/100')
    term = term.replace('rad', 'radians')
    term = term.replace('mod', '%')

    # 函数替换为 math函数
    functions = ['sin', 'cos', 'tan', 'sqrt', 'pi', 'radians', 'e']
    for f in functions:
        if f in term.lower():
            with_math = 'math.' + f
            term = term.replace(f, with_math)

    # 计算
    try:
        term = eval(term)
    except ZeroDivisionError:
        print("不能除零")
        return ""
    except NameError:
        print('非法输入')
        return ""
    except AttributeError as a:
        print(str(a))
        return ""
    except SyntaxError:
        print("表达式非法")
        return ""
    return term


def result(term):
    print("\n" + str(calc(term)))


def main():
    print("\n计算器\n例如: sin(rad(90)) + 50% * (sqrt(16)) + round(1.42^2) - 12mod3\n输入 quit 结束")

    if sys.version_info.major >= 3:
        while True:
            k = input("\n表达式： ")
            if k == 'quit':
                break
            result(k)

    else:
        while True:
            k = input("\nWhat is ")
            if k == 'quit':
                break
            result(k)


main()
