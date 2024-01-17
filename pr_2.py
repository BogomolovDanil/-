import math

#1
x=14.26
y=-1.22
z=3.5*10**-2
s=(((2*math.cos(x-2/3))/(1/2+math.sin(y)**2))*(1+((z**2)/(3-z**2/5))))
print(s)

#2
x=-4.5
y=0.75*10**-4
z=-0.845*10**2
s=((9+(x-y)**2)**(1/3))/(x**2+y**2+2)-math.exp(abs(x-y))*math.tan(z)**3
print(s)

#3
x=3.74*10**-2
y=-0.825
z=0.16*10**2
s=((1+(math.sin(x+y))**2)/(abs(x-((2*y)/(1+x**(2)*y**(2))))))*x**(abs(y))+math.cos(math.atan(1/z))
print(s)

#4
x=0.4*10**4
y=-0.875
z=-0.475*10**-3
s=(abs(math.cos(x)-math.cos(y)))**(1+2*(math.sin(y))**2)*(1+z+(z**(2)/2)+(z**(3)/3)+(z**(4)/4))
print(s)

#5
x=-15.246
y=4.642*10**-2
z=21
s=math.log(y**(-(abs(x))**(1/2)))*(x-y/2)+(math.sin(math.atan(z)))**2
print(s)

#6
x=16.55*10**-3
y=-2.75
z=0.15
s=math.sqrt(10*(x**(1/3)+x**(y+2)))*((math.asin(z))**(2)-abs(x-y))
print(s)

#7
x=0.1722
y=6.33
z=3.25*10**-4
s=5*math.atan(x)-(1/4)*math.acos(x)*(x+3*abs(x-y)+x**2)/(abs(x-y)*z+x**2)
print(s)

#8
x=-2.235*10**-2
y=2.23
z=15.221
s=(math.exp(abs(x-y))*(abs(x-y))**(x+y))/(math.atan(x)+math.atan(z))+(x**6+(math.log(y))**2)**(1/3)
print(s)

#9
x=1.825*10**2
y=18.225
z=-3.298*10**-2
s=abs(x**(y/x)-(y/x)**(1/3))+(y-x)*(math.cos(y-(z/(y-x)))/(1+(y-x)**2))
print(s)

#10
x=3.981*10**-2
y=-1.625*10**3
z=0.512
s=2**(-x)*math.sqrt(x+(abs(y))**(1/4))*(math.exp(x-1/(math.sin(z))))**(1/3)
print(s)

#12
x=3.251
y=0.325
z=0.466*10**4
s=2**(y**(x))+(3**(x))**(y)-((y*(math.atan(z)-1/3))/(abs(x)+1/(y**(2)+1)))
print(s)

#13
x=17.421
y=10.365*10**-3
z=0.828*10**5
s=((y+(x-1)**(1/3))**(1/4))/(abs(x-y)*((math.sin(2))**(2)+math.tan(z)))
print(s)

#14
x=12.3*10**-1
y=15.4
z=0.252*10**3
s=(y**(x+1)/((abs(y-2))**(1/3)+3))+((x+y/2)/(2*abs(x+y)))*(x+1)**(-1/math.sin(z))
print(s)

#15
x=2.444
y=0.869*10**(-2)
z=-0.13*10**(3)
s=((x**(y+1)+math.exp(y-1))/(1+x*abs(y-math.tan(z))))*(1+abs(y-x))+((abs(y-x))**2)/2-((abs(y-x))**3)/3
print(s)


