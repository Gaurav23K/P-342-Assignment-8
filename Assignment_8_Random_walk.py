import random
import matplotlib.pyplot as plt
import math
import you_can

R_rms = []
Radial = []
Displacement_x = []
Displacement_y = []

plt.figure()
repeat = 100
total_steps = 100
kaa = you_can.random_walk(repeat, total_steps)         #Calling random_walk function
R_rms.append(kaa[2])
Radial.append(kaa[3])
Displacement_x.append(kaa[4])
Displacement_y.append(kaa[5])
plt.subplot(2,3,1)
plt.title("(i) N = "+str(total_steps))
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
with open('N(100).txt', 'w') as a:
    for j in range(5):
        plt.plot(kaa[0][j], kaa[1][j])              #Plot for N = 100
        a.writelines("[")
        a.writelines("%s," % i for i in kaa[0][j])
        a.writelines("]")
        a.writelines("\n""\n""\n")
        a.writelines("[")
        a.writelines("%s," % i for i in kaa[1][j])
        a.writelines("]")


kaa = you_can.random_walk(repeat, 5*total_steps)        #Calling random_walk function
R_rms.append(kaa[2])
Radial.append(kaa[3])
Displacement_x.append(kaa[4])
Displacement_y.append(kaa[5])
plt.subplot(2,3,2)
plt.title("(ii) N = "+str(5*total_steps))
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
with open('N(500).txt', 'w') as a:
    for j in range(5):
        plt.plot(kaa[0][j], kaa[1][j])                #Plot for N = 500
        a.writelines("[")
        a.writelines("%s," % i for i in kaa[0][j])
        a.writelines("]")
        a.writelines("\n""\n")
        a.writelines("[")
        a.writelines("%s," % i for i in kaa[1][j])
        a.writelines("]")


kaa = you_can.random_walk(repeat, 10*total_steps)          #Calling random_walk function
R_rms.append(kaa[2])
Radial.append(kaa[3])
Displacement_x.append(kaa[4])
Displacement_y.append(kaa[5])
plt.subplot(2,3,3)
plt.title("(iii) N = "+str(10*total_steps))
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
with open('N(1000).txt', 'w') as a:
    for j in range(5):
        plt.plot(kaa[0][j], kaa[1][j])                     #Plot for N = 1,000
        a.writelines("[")
        a.writelines("%s," % i for i in kaa[0][j])
        a.writelines("]")
        a.writelines("\n""\n")
        a.writelines("[")
        a.writelines("%s," % i for i in kaa[1][j])
        a.writelines("]")


kaa = you_can.random_walk(repeat, 50*total_steps)           #Calling random_walk function
R_rms.append(kaa[2])
Radial.append(kaa[3])
Displacement_x.append(kaa[4])
Displacement_y.append(kaa[5])
plt.subplot(2,3,4)
plt.title("(iv) N = "+str(50*total_steps))
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
with open('N(5000).txt', 'w') as a:
    for j in range(5):
        plt.plot(kaa[0][j], kaa[1][j])                     #Plot for N = 5,000
        a.writelines("[")
        a.writelines("%s," % i for i in kaa[0][j])
        a.writelines("]")
        a.writelines("\n""\n")
        a.writelines("[")
        a.writelines("%s," % i for i in kaa[1][j])
        a.writelines("]")


kaa = you_can.random_walk(repeat, 100*total_steps)           #Calling random_walk function
R_rms.append(kaa[2])
Radial.append(kaa[3])
Displacement_x.append(kaa[4])
Displacement_y.append(kaa[5])
plt.subplot(2,3,5)
plt.title("(v) N = "+str(100*total_steps))
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
with open('N(10000).txt', 'w') as a:
    for j in range(5):
        plt.plot(kaa[0][j], kaa[1][j])                     #Plot for N = 10,000
        a.writelines("[")
        a.writelines("%s," % i for i in kaa[0][j])
        a.writelines("]")
        a.writelines("\n""\n")
        a.writelines("[")
        a.writelines("%s," % i for i in kaa[1][j])
        a.writelines("]")
plt.tight_layout()
plt.show()


Root_N = [10, math.sqrt(500), math.sqrt(1000), math.sqrt(5000), 100]
plt.plot(Root_N, R_rms,marker = 'o',markerfacecolor = 'cyan')
plt.xlabel("$N^{1/2}$")
plt.ylabel("$R_{rms}$")
plt.show()

print("Radial distance for different random walks(N = (100, 300, 500, 1000, 10000 )):", Radial)
print("R_rms for different random walks", R_rms)
print(f"The average x & y displacement for random walks(N = (100, 300, 500, 1000, 10000)) is: $delta$ X = ",Displacement_x, "$delta$ Y = ", Displacement_y )
print("Values of root N", Root_N)

"""*****************************************************OUTPUT*************************************************************

Radial distance for different random walks: [62.356870327488586, 196.95023483097015, 337.1730782143834, 651.4548346063843, 6705.270887477553]
R_rms for different random walks [66.61089769800725, 212.31516985717315, 362.06283734784796, 707.1567792716653, 7167.492280853139]
Values of root N [10, 17.320508075688775, 22.360679774997898, 31.622776601683793, 100]


"""





