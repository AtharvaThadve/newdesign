import math

mag=[]
sine=[]
cos=[]
fnum=int(input("Number of frces:"))
for i in range(0,fnum):
   m=float(input("Mag:"))
   a=float(input("Angle:"))
   mag.append(m)
   sine.append(math.sin(math.radians(a)))
   cos.append(math.cos(math.radians(a)))

print(mag)
print(sine)
print(cos)

result1=[]
for i1,i2 in zip(mag,sine):
   result1.append(i1*i2)
result2=[]
for i1,i2 in zip(mag,cos):
   result2.append(i1*i2)


fx=sum(result1)
fy=sum(result2)
print(result1)
print(result2)
print(fx)
print(fy)

Resultant=math.sqrt((fx*fx)+(fy*fy))
print(Resultant)
alpha=math.atan(fy/fx)
print(alpha)


