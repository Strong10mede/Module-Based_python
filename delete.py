import matplotlib.pyplot as plt  //i am raghav sethi
from matplotlib import style

#normal
plt.plot([1,2,3],[4,3,5])
plt.show()

#normal2
x=[5,8,11]
y=[6,8,5]
plt.title("Graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x,y)
plt.show()

#usingstyle
style.use('ggplot')
x1=[2,4,6]
y1=[6,2,3]
plt.plot(x,y,'g',label='One Time',linewidth=5)
plt.plot(x1,y1,'c',label='Two Time',linewidth=5)
plt.title("Graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True,color='k')
plt.legend()
plt.show()
