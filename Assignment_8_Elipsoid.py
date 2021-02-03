import matplotlib.pyplot as plt
import you_can
import math

N = [100, 500, 1000, 2000, 4000, 8000, 10000, 20000, 30000, 40000, 50000]
total_points = 10000
Cast = []                       #Stores calculated volume
error_list = []
Vol = 4/3* math.pi*1*1.5*2      #Analytical volume of ellipsoid


# (d) part

op = you_can.ellipsoid(total_points, 1)           #Calling ellipsoid function


# (a) part

i = 0
while i <= 10:
    # for j in range(N[i]):
    gg = you_can.ellipsoid(N[i], 0)                 #Calling ellipsoid function
    Cast.append(gg)
    i += 1


# (b) part

plt.figure()
plt.title("Volume of Ellipsoid vs No. of points")
plt.axhline(y=Vol)
plt.plot(N, Cast, marker = 'o',markerfacecolor = 'cyan')
plt.xlabel("$N$")
plt.ylabel("Volume of Ellipsoid")
plt.show()


# (c)

for i in range(len(Cast)):
    error = abs(Vol - Cast[i])/Vol
    error_list.append(error)

plt.figure()

plt.plot(N, error_list, marker = 'o',markerfacecolor = 'cyan')
plt.axhline(y = 0)
plt.xlabel("$N$")
plt.ylabel("Fractional Error")
plt.title("Fractional error vs No. of counts")
plt.show()

print("The set of 10 trials are : ",N)
print("Fractional error for 10 trials : ",error_list)
print("The volume of ellipsoid is: ", op," and the analytical value is : ", Vol)


'''
************************************OUTPUT*****************************************

The set of ten trials are :  [100, 500, 1000, 2000, 4000, 8000, 10000, 20000, 30000, 40000, 50000]
Fractional error for 10 trials : [0.06416893461965541, 0.014512592374984016, 0.008405719430248934, 0.0064958601131461175, 0.0026761414789406262, 0.016899916521362537, 0.0011435771552648654, 0.006109211379732019, 0.001461887041448621, 0.010220085781496554, 0.000265041869397502]
The volume of ellipsoid is:  12.6432 and the analytical value is :  12.566370614359172

Process finished with exit code 0

'''