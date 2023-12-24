import matplotlib.pyplot as plt

a = 5
b = 20
L = 30
Ma = 80
Mb = 40
w = 75


By = (Ma + w*(a+(b-a)/2) - Mb) / L
Ay = w - By

########  1. KESME  ########

K1 = Ay

def Mk1(x):
    return Ma + K1*x


########  2. KESME  ########

def K2(x):
    return Ay - w * (x-a)

def Mk2(x):
    return Ma - w * ((x-a)/2) + Ay*x


########  1. KESME  ########

K3 = Ay

def Mk3(x):
    return Ma + K3*x


########### GRAFİK LİSTELERİ HAZIRLMA  ############

x_list_kesme = [*range(L)] # K1 K2 K3
y_list_kesme = []

x_list_eğilme = [*range(L)] # Mk1 Mk2 Mk3
y_list_eğilme = []

for i in range(L):
    
    if i < a:

        y_list_kesme.append(K1)
        y_list_eğilme.append(Mk1(i))

    elif i > a and i < b:
        
        y_list_kesme.append(K2(i))
        y_list_eğilme.append(Mk2(i))

    else:
        
        y_list_kesme.append(K3)
        y_list_eğilme.append(Mk3(i))



plt.subplot(2, 1, 1)
plt.plot(x_list_eğilme, y_list_eğilme)
plt.title('Eğilme Momenti')


plt.subplot(2, 1, 2)
plt.plot(x_list_kesme, y_list_kesme)
plt.title('Kesme Momenti')

plt.subplots_adjust(hspace=0.5)

plt.show()












