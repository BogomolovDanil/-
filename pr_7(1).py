from math import sqrt, pi
print("1-прямоугольник, 2-треугольник, 3-круг")
figure= input("Выберите фигуру: ")
match figure:
	case '1':
		print("Длины сторон прямоугольника:")
		a=float(input("a = "))
		b=float(input("b = "))
		print("Площадь: %.2f" % (a*b))
	case '2':
		print ("Длины сторон треугольника:")
		a=float(input("a= "))
		b=float(input("b= "))
		c=float(input("c= "))
		p=(a+b+c)/2
		s=sqrt(p*(p-a)*(p-b)*(p-c))
		print("Площадь: %2f" % s)
	case '3':
		r=float(input("Радиус круга R= "))
		print("Площадь %2f" %(pi*r**2))
	case _:
		print("Ошибка ввода")
