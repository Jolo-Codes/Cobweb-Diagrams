import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [2,4,6,8,10]

# plt.plot(x,y)
# plt.plot(y,x)
# plt.plot(x)

# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("SImple Plot!")


# # plt.show() displays the plot

# #we can also do this with a subplot, not the gloabl plot
# #This is object oriented

# fig, ax = plt.subplots()
# ax.plot(x,y)
# ax.set_xlabel("joel")
# ax.set_ylabel("bakka")

# plt.show()

x = np.linspace(0,10,100)

#creates a numpy list with 100 elements 0 10 inclusive.

#If I then do list +1, it adds 1
#if I do sin, it sines all
#Note, even if I put in normal; it returns a np list, and it works for nomral


# y = np.sin(x)

# #100 data values, sinx each time ,y against 

# plt.plot(x,y)
# plt.xlabel("Hi")
# plt.ylabel("Bye")

# plt.show()