def calculate_rectangle_area(length, width):
    area = length * width
    return area

length = float(input("请输入长方形的长度："))
width = float(input("请输入长方形的宽度："))

result = calculate_rectangle_area(length, width)
print("长方形的面积为：", result)
