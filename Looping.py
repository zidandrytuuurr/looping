#!/usr/bin/env python
# coding: utf-8

# In[1]:


# mencetak angka 1 - 10

for i in range(1,11):
    print(i, end=" ")


# In[5]:


# mencetak angka 10 20 30 --- 100

for i in range(10,101,10):
    print(i, end=" ")


# In[6]:


# mencetak angka 10 20 30 --- 100

for i in range(1,11):
    print(i * 10, end =" ")


# In[10]:


# mencetak angka 10 9 8 7 ... 1

for i in range(1,11):
    print(11 - i, end =" ")


# In[11]:


for i in range(10,0,-1):
    print(i, end=" ")


# In[22]:


# mencetak 1 -2 3 -4 5 -6 ... 10
sign = -1
for i in range(1,11):
    sign = sign * -1
    print(sign *i, end=" ")
    


# In[25]:


#mencari bilangan faktorial
# input = 3, output = 3 * 2 * 1 = 6
# input = 4, output = 4 * 3 * 2 * 1 = 24

bil = int(input('Isikan bilangan:'))

hasil = 1

for i in range(1, bil+1):
    hasil = hasil * i
    
print(f"{bil}! adalah {hasil}")


# In[34]:


#mencari bilangan faktorial
# input = 3, output = 3 * 2 * 1 = 6
# input = 4, output = 4 * 3 * 2 * 1 = 24

bil = int(input('Isikan bilangan:'))

hasil = 1
label =""
for i in range(1, bil+1):
    hasil = hasil * i
    if  i < bil:
        label = label + str((bil+1) - i) + " * "
    else:
        label = label + str(( bil+1)- i)
print(f"{bil}! adalah {hasil}")
print(f"{label} = {hasil}")


# In[35]:


#menghitung pangkat
bilangan = int(input('masukan bilangan: '))
pangkat =int(input('masukan pangkat '))

hasil = bilangan

for i in range (pangkat - 1):
    hasil *=bilangan
print(f"{bilangan}^{pangkat} = {hasil}")


# In[4]:


#mengecek bilangan prima atau bukan
#Bil. prima adalah bilangan yang
#hanya habis dibagi dengan  1 dan bilangan itu sendiri => 2 faktor
bil = int(input("masukan bilangan prima:"))
keterangan = 
for i in range(1, bil + 1):
        sisa = bil % i
        if sisa == 0:
            jumlah = jumlah + 1
if jumlah == 2:
    print(f"{bil} adalah bilangan prima")

else:
    print(f"{bil} adalah bilangan bukan prima")


# In[3]:


#break dan continue

for i in range(1,100):
    print(i, end = " ")
    if i==5:
        break
print()

for j in range(1,10):
    if j == 5:
        continue
    print(j, end=" ")


# In[ ]:


#looping untuk string, menghitung huruf vokal a=?, i=?, u=?, e=?, o=?
kalimat = input("isikan kalimat : ")

vokal_a = 0
vokal_i = 0
vokal_u = 0
vokal_e = 0
vokal_o = 0
for i in kalimat:
    if i=='a':
        vokal_a += 1
    elif i=='i':
        vokal_i += 1
    elif i=='u':
        vokal_u += 1
    elif i=='e':
        vokal_e += 1
    elif i=='o':
        vokal_o += 1
        
print(f"jumlah a:{vokal_a}\njumlah huruf i:{vokal_i}\njumlah huruf u:{vokal_u}\njumlah huruf e:{vokal_e}\njumlah huruf o:{vokal_o}")
total = vokal_a+vokal_i+vokal_u+vokal_e+vokal_o


# In[ ]:


#kalimat palindrome atau bukan
#palindrome adalah kalimat yamg dibaca dari kiri ke kanan
#katak => palindrome
#kasur rusak
ulang = "Y"
while(ulang=="Y"):
    kalimat = input('isikan kalimat:')
    panjang = len(kalimat)

    for i in range(0,panjang):
        kika = kalimat [i].lower()
        kaki = kalimat [panjang - i - 1].lower()
        if kika != kaki:
            keterangan = "BUKAN PALINDROME"
            break
    print(f"{keterangan}")    
    
    jawab=""
    while(jawab!="Y" and jawab !="T"):
        ulang = input("Apakah Mau Mengulang Program(Y/t)?: ")
    ulang == jawab


# In[ ]:


#nested FOR

for i in range(1,5):
    for j in range(1,5):
        print(f"i:{i} dan j:{j}")

