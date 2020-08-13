#!/usr/bin/env python
# coding: utf-8

# In[7]:


from sympy.ntheory import factorint
q=int(input("Give me the number q=")) 
fact=factorint(q)        #We factor the number q=p_1^{n_1}*p_2^{n_2}*...
p_1=list(fact.keys())    #We create a list with keys to be the the numbers p_1,p_2,...
n_1=list(fact.values())  #We create a list with values to be the the numbers n_1,n_2,...
p=int(p_1[0])            #We define p=p_{1}
n=int(n_1[0])            #We define n=n_{1}
if q!=p**n:              #Check if the number q=p_{1}[0]**n_{1}[0]=p**n.
    print("The number "+str(q)+" is not a prime power")
    print("Run again the code and imput a prime power")
else:
    print("The number "+str(q)+" is a prime power")
    print("The prime number p="+str(p))
    print("The natural number n="+str(n))


# In[ ]:





# In[ ]:




