#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np


# In[33]:


def search_cube(s,ch):
    for i in range(len(s)):
        if s[i] == ch and s[i+1]!="'":
            return 1
        elif s[i]==ch and s[i+1]=="'":
            return 2
    return 0


# In[34]:


def get_cubelist(n,s):
    alpha = []
    for i in range(n):
        alpha.append(chr(97+i))
    arr = []
    for i in range(len(s)):
        cube = s[i] + ' '
        pcn = []
        for j in range(n):
            pcn.append(search_cube(cube, alpha[j]))
        arr.append(pcn)
    return arr


# In[35]:


def get_cofactors(arr1, arr2):
    co_factors = [row[:] for row in arr1]
    for i in range(len(arr2[0])):
        var = arr2[0][i]
        if var!=0:
            j=0
            while(j<len(co_factors)):
                x = co_factors[j]
                if x[i] == var or x[i]==0:
                    x[i] = 0
                    j = j+1
                else:
                    co_factors.remove(x)
    return co_factors


# In[36]:


def get_func(arr,n):
    alpha = []
    for i in range(n):
        alpha.append(chr(97+i))
    s = ""
    for x in arr:
        if all(x == np.zeros(n)):
            s = "1"
            break
        for i in range(len(x)):
            if x[i]==1:
                s = s+alpha[i]
            elif x[i]==2:
                s = s+alpha[i] + "'"
        s = s+ "+"
    if s=="":
        s = "0"
    if s[-1]=="+":
        s = s[0:len(s)-1]
    return s


# In[37]:


class Node:
    def __init__(self, initval = None):
        self.name = initval
        self.hi = None
        self.lo = None
        return


# In[38]:


zero_node = Node("0")
one_node = Node("1")


# In[39]:


def search_unique_table(key, node):
    if key in unique_table.keys():
#        print(1)
        return unique_table[key]
    else:
        unique_table[key] = node
        return node


# In[40]:


def ITE(function, variable_order, i, n):
    top_var = [[x for x in variable_order[i]]]
#    print(get_func(top_var, n))
    
    fa_cube = get_cofactors(function, top_var)
    fa = get_func(fa_cube,n)
#    print(fa)
    
    var_bar = [x for x in variable_order[i]]
    for j in range(len(var_bar)):
        if var_bar[j]==1:
            var_bar[j] = 2
    var_bar = [var_bar]
    
    fa_bar_cube = get_cofactors(function, var_bar)
    fa_bar = get_func(fa_bar_cube, n)
#    print(fa_bar)
    
    key = get_func(top_var, n)
    key = key + "," + fa + "," + fa_bar
#    print(key)
    
    node = Node(get_func(top_var, n))
    if fa=="0":
        node.hi = zero_node
    if fa=="1":
        node.hi = one_node
    if fa_bar=="0":
        node.lo = zero_node
    if fa_bar == "1":
        node.lo = one_node
        
    if node.hi == None:
        node.hi = ITE(fa_cube, variable_order, i+1, n)
    if node.lo == None:
        node.lo = ITE(fa_bar_cube, variable_order, i+1, n)
    
    node = search_unique_table(key, node)
    if node.hi == node.lo:
        return node.hi
    return node


# In[41]:


def printPostorder(root): 
  
    if root: 
  
        # First recurse on left child 
        printPostorder(root.lo) 
  
        # the recurse on right child 
        printPostorder(root.hi) 
  
        # now print the data of node 
        print(root.name, end= " ")


# In[42]:


n = int(input("Enter number of Variables: "))
function = input("Enter the function(SOP form): ").split("+")
func_cubelist = get_cubelist(n, function)
print(get_func(func_cubelist,n))

print("Enter the variable ordering: ")
order = []
for i in range(n):
    print(i+1, ": ", end = " ")
    order.append(input().strip())
print(order)

variable_order = get_cubelist(n, order)

print(variable_order)

unique_table = {}

print(get_func(func_cubelist, n))
node = ITE(func_cubelist, variable_order, 0, n)


# In[43]:


print("Order: node, node.hi, node.lo")
for key in unique_table.keys():
    print(key)


# In[44]:


print("Post-Order Traversal")
printPostorder(node)






