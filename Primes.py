import numpy as np 
import matplotlib.pyplot as plt

#defining a function to convert polar coordinates into cartesian coordinates since the latter are plotted in matplotlib.

def polar2cart(r,theta):
    '''
This function converts plane polar coordinates(r,theta) to cartesian coordinates (x,y),using the formula :-

x=rcostheta
y=rsintheta


Note: np.cos is the mathematical function Cos(theta)
np.sin is the mathematical function Sin(theta)
theta is an angle in radians
    '''
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    return x,y

#integer range between 0 and n2

n2 = 10000    

#plotting parameters   

plt.figure(figsize=(10,10))                                                               
ax=plt.axes()    
ax.axis('off') 
ax.set_title('Primes between 0 and ' +str(n2))

#program to compute primes between 0 and n2, the outer foor loop assigns a value to the varible n. Let's say
#n = 6, this value of n is divided by every number in the range (2 to n-1) inside the inner for loop until a factor of
#n is found i.e when the modulo operator '%' == 0. As soon as this condition is satisfied the loop breaks and prints 'n, not prime'. 
#(in our example, for n = 6, since 6 is divisible by two numbers (2 & 3) in the range 2 - 5,the condition for prime numbers is not satisfied.)
#if no factor is found in the assigned range, the else statement which is a part of the outer for loop is executed and prints 'n, prime'. After
#which the next value is assigned to n and this process repeats.

for n in range(0,n2+1):                                                
    for x in range(2,n):
        if n%x == 0:
            print(n , 'not prime')  
            break
                    
    else:
        print(n ,'prime')
        px , py = polar2cart(n,n)
        ax.plot(px,py,'.')

# when the else statement part of the loop is executed i.e. a prime is found, the function polar 2 cart converts the 
# plane polar coordinates to cartesian coordinates to plot the prime.


plt.show()
        
