'''
    正弦函数：sine function, y=sin(x)
    余弦函数: cosine function, y=cos(x)
    正切函数: tangent function, y=tan(x)
'''
import math

# page 178, example 1
x = 5 / 3 * math.pi
y_sin = math.sin(x)
print(y_sin)
y_cos = math.cos(x)
print(y_cos)
y_tan = math.tan(x)
print(y_tan)


# page 179, exercise 1
def trigonomy(x):
    return {
        "x": x,
        "sin": math.sin(x),
        "cos": math.cos(x),
        "tan": math.tan(x)
    }

y1 = trigonomy(0)
print(y1)
y2 = trigonomy(math.pi / 2)
print(y2)
y3 = trigonomy(math.pi)
print(y3)
y4 = trigonomy(math.pi * 3 / 2)
print(y4)

