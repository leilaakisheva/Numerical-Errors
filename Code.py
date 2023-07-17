import numpy as np
import scipy.special as scs
import matplotlib.pyplot as plt
import math
# %matplotlib inline

#defining function e^-x
def e(x,N):
  if N<0: #It is not possible to take negative value as factorial
    print("Wrong input of the order of series. Please try again.")
    N = int(input('Enter the order of Maclaurin series: '))
  elif int(N)!=N: #checking if the inputed number is an integer value
    print("Wrong format of the number. Please enter the int value.")
    N = int(input('Enter the order of Maclaurin series: '))
  return np.sum([((((-x)**i))/math.factorial(i)) for i in range(N+1)])

#Computing error using the expected value (true value) of exp and computed in the code
#delta variable represents a relative error
def error(x, t):
  V_e = np.exp(-x)
  V_a = e(x,t)
  delta = abs((V_a-V_e)/V_e)
  return delta

#defining a function to create a plot
def plot(val, N):
  x = np.arange(1, N+1, 1)
  y = np.zeros(N)
  V_e = np.exp(-val)
  V_a = np.zeros(N)
  for n in range(1,N+1):
    V_a[n-1] = e(val,n)
    y[n-1] = error(val, n)
    if y[n-1]<10**(-14) and y[n-1]>=10**(-15):#to find the values where the relative error is 10^-15 order
          print("For x =", val, ", at the value of order n =", n, ", the relative error attain the value of ", error(val, n))
    if y[n-1]==0: #since the python cannot go further 10^-17 it sometimes give 0 as the value
      y[n-1]=y[n-2]
  plt.plot(x,y)
  plt.yscale("log")
  plt.xlabel("Value of order")
  plt.ylabel("Relative error")

"""Now, I test my code using random input values:"""

#inputing values of variables
t = int(input('Enter the order of Maclaurin series: '))
x = float(input('Enter the va2lue of x: '))
print("The value of Taylor approximation is", e(x,t))
print('Expected value of exp(-x)', np.exp(-x))
print('Relative error is ', error(x, t))

N=29
plot(0.3, N)
plot(1, N)
plot(2.0, N)
plt.legend(['x=0.3', 'x=1', 'x=2'])
