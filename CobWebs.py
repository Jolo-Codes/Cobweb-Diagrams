import matplotlib.pyplot as plt
import numpy as np
import sympy as sp # importing modules
Iter_in_graph = True
buffer = 0

x = sp.symbols("x")
equation = input("Define your iterative function > ") # Using sympy, I will convert this to a normal function
iterable = sp.sympify(equation)
iter_function = sp.lambdify(x,iterable,"numpy")

#Now, I have a function such that I plug in x, and I get the y

repeats = int(input("Define how many times you'd like to repeat (the next 3 inputs must be integers) > "))
upper_lim = int(input("Define the upper value that you want the line y = x to go to (and, in turn, the lower, + maximum y of the iterable function)> "))
inital_x = int(input("Define the inital x > "))
inital_y = iter_function(inital_x)

#Defining a few key variables

fig, axs = plt.subplots() #Defining the plot
axs.grid(True)

#First, I will add the line y = x
axs.axline((-upper_lim,-upper_lim),slope=1, label ="y=x",color="red")

#Next, I will plot the reproduction curve;
x_values = np.linspace(0,upper_lim,upper_lim*10)
axs.plot(x_values,iter_function(x_values),label = equation,color="blue")

#Next, I will start to draw the cobweb, starting with step 3: draw from inital x, to line on reproduction

axs.plot([inital_x, inital_x],[0,inital_y])

#Next, I define the iteration structure, that performs steps 4-5
#It starts with drawing a horizontal line to y = x
#First, I will define the first values of x_iter and y_iter outside of the function

x_iter_values = inital_x
y_iter_values = inital_y

for repeat in range(repeats):
    #To draw horizontal line, as y = x, we first plot the current x and current y, then join it to the same y, but the x on the line y = x
    new_x = y_iter_values
    new_y = iter_function(y_iter_values)

    if new_x > upper_lim or new_y > upper_lim or new_x < -upper_lim or new_y < -upper_lim:
        Iter_in_graph = False
        break # this ensures that the graph won't bug out.

    axs.plot([x_iter_values,new_x] ,[y_iter_values,y_iter_values])

    #This performs step 5. We start with where we ended, keep the x the same, and find what the y would be by plugging in x

    axs.plot([new_x,new_x],[y_iter_values,new_y])

    #We then update the x and y based on the final points, to allow repeats.
    x_iter_values = new_x
    y_iter_values = new_y

#Finally, I want to reachor the camera to ensure that it looks cool.
if Iter_in_graph and (new_x > inital_x and new_y > inital_y):
    buffer = new_x*0.15
    axs.set_xlim(-abs(new_x) - buffer,abs(new_x) + buffer)
    axs.set_ylim(-abs(new_y) - buffer,abs(new_y) + buffer)

  
elif not Iter_in_graph and (new_x > inital_x and new_y > inital_y):
    buffer = new_y*0.15
    axs.set_xlim(-abs(x_iter_values) - buffer,abs(x_iter_values) + buffer)
    axs.set_ylim(-abs(y_iter_values) - buffer,abs(y_iter_values) + buffer)

else:
    buffer = inital_x*0.15
    axs.set_xlim(-abs(inital_x) - buffer,abs(inital_x) + buffer)
    axs.set_ylim(-abs(inital_x) - buffer,abs(inital_x) + buffer)   


axs.legend()
plt.show()



