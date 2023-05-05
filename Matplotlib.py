# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([1,2,3,4,5,6,7])
# ypoints = np.array([0,3,7,8,12,15,17])
# y1points = np.array([1,2,3,4,5,6,7])
# x1points = np.array([0,3,7,8,12,15,17])
#
# font1 = {'family':'serif','color':'blue','size':15}
# font2 = {'family':'serif','color':'darkred','size':10}
#
# plt.plot(xpoints, ypoints, color='r',marker ='o',linewidth=3)
# plt.plot(x1points, y1points, color='#4CAF50',marker ='o')
# plt.title("Sports Watch Data",fontdict = font1,loc = 'left')
# plt.xlabel("Average Pulse",fontdict = font2)
# plt.ylabel("Calorie Burnage",fontdict = font2)
#
# plt.grid(color = 'blue', linestyle = '--', linewidth = 0.5)
# plt.show()


'''
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()
'''

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
'''


''''
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90,shadow = True)
plt.legend()
plt.show()
'''
