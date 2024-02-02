#!/usr/bin/env python
# coding: utf-8

# In[1]:


upper_bound_strng = input('enter an upper bound for a check: ')
print('between 1 and',upper_bound_strng,'there are')

if upper_bound_strng.isdigit():
    upper_bound = int(upper_bound_strng)
    
    if upper_bound >= 1:
        deficient_numbers = 0
        perfect_numbers = 0
        abundant_numbers = 0
        
        for num in range(1, upper_bound + 1):
            sum=0
            
            for i in range(1,num):
                if num % i == 0:
                    sum += i
            
            if sum == num:
                perfect_numbers += 1
            elif sum < num:
                deficient_numbers += 1
            else:
                abundant_numbers += 1
                
        print(deficient_numbers,'deficient numbers')
        print(perfect_numbers,'perfect numbers')
        print(abundant_numbers,'abudant numbers')

    


# In[ ]:




