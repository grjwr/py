# -*- coding: utf-8 -*-
"""Copy of Daa P1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_WpuuQPFmU98Kqgc_eL2n3cQeEQGGQI0

## Experiment 1: 
### Implementation and Time analysis of Factorial program using iterative and recursive method. Optimize it using dynamic programming.

**7 Steps to solve a Dynamic Programming problem**
In the rest of this post, I will go over a recipe that you can follow to figure out if a problem is a “DP problem”, as well as to figure out a solution to such a problem. Specifically, I will go through the following steps:

*   How to recognize a DP problem
*   Identify problem variables
*   Clearly express the recurrence relation
*   Identify the base cases
*   Decide if you want to implement it iteratively or recursively
*   Add memoization
*   Determine time complexity

*[ref: https://www.freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e/]*
"""

# Factorial iterative method

# %%time
fact = 1
n=int(input('enter the nummber n = '))
for i in range(1,n+1):
      fact*=i
print('Factorial of n = ',fact)

"""%%timeit
fact = 1
n=int(input('enter the nummber n = '))
for i in range(1,n+1):
      fact*=i
print('Factorial of n = ',fact)

## Consider calculating the fibonacci sequence:

### Pure recursion:


```
int fib(int x)
{
    if (x < 2)
        return 1;

    return fib(x-1) + fib(x-2);
}
```

### Recursion with memoization/DP:



```
void fib(int x)
{
    static vector<int> cache(N, -1);

    int& result = cache[x];

    if (result == -1)
    {
        if (x < 2)
            result = 1;
        else
            result = fib(x-1) + fib(x-2);
    }

    return result;
}
```

### The following would also be considered DP, but without recursion:

```
int fibresult[N];

void setup_fib()
{
    fibresult[0] = 1;
    fibresult[1] = 1;
    for (int i = 2; i < N; i++)
       fibresult[i] = fibresult[i-1] + fibresult[i-2];
}

int fib(int x) { return fibresult[x]; }
```

###Also the following is neither recursion nor DP:

```
int fib(int x)
{
    int a = 1;
    int b = 1;
    for (int i = 2; i < x; i++)
    {
        a = a + b;
        swap(a,b);
    }
    return b;
}
```
"""

# Pure recursion:
# %%time
#n=int(input('enter the nummber n = '))
n=5
def fact(n):
  if(n<1):
    return 1
  return n*fact(n-1)
  
print('Factorial of given no. is : ',fact(n))

#Recursion with memoization/DP:
# %%time
#n=int(input('enter the nummber n = '))
fl=[]
ans=0
n=5
def fact(n):
  if(n<1):
    return 1
  else:
    ans = n*fact(n-1)
    fl.append(ans)
    return ans
print('Factorial of given no. is : ',fact(n))

# DP, but without recursion:

# %%time
ans =[]
#ans.append(5)
#n=int(input('enter the nummber n = '))

fact = 1
n=5

for i in range(1,n+1):
  fact*=i
  if fact in ans:
    fact= ans[ans.index(ans)]*i
    ans.append(fact)
  else:
    ans.append(fact)
print('Factorial of given no. is : ',ans[-1])

"""%%time
start = time.time()
t=[]
fact = 1
n=[2,4,8,16,32,64,128,256,512,1024,2056,4086]
for i in n:
      fact*=i
print('Factorial of n = ',fact)
"""

import time
import matplotlib.pyplot as plt
#import numpy as np

# Factorial Iterative method
start = time.time()
t1=[]
fact = 1
n1=[]
for i in range(1,1024,2):
  n1.append(i)
for i in n1:
  for j in range(1,i):
      fact*=j
  stop = time.time()
  t1.append(stop-start)

# Factorial using DP
start2 = time.time()
t2=[]
ans=[]
fact = 1
for i in n1:
  fact*=i
  if fact in ans:
    fact= ans[ans.index(ans)]*i
    ans.append(fact)
  else:
    ans.append(fact)
  stop = time.time()
  t2.append(stop-start)
#print('Factorial of given no. is : ',ans[-1]) 
print(t1)
print(t2)
 
plt.plot(n1, t1,alpha=0.7)
plt.plot(n1, t2,alpha=0.7)


plt.show()

import time
import matplotlib.pyplot as plt
#import numpy as np

# Factorial Iterative method
start = time.time()
t1=[]
fact = 1
n1=[]
for i in range(1,1000,2):
  n1.append(i)
for i in n1:
  for j in range(1,i):
      fact*=j
  stop = time.time()
  t1.append(stop-start)

# Factorial using DP
start2 = time.time()
t2=[]
ans=[]
fact = 1
for i in n1:
  fact*=i
  if fact in ans:
    fact= ans[ans.index(ans)]*i
    ans.append(fact)
  else:
    ans.append(fact)
  stop = time.time()
  t2.append(stop-start)
#print('Factorial of given no. is : ',ans[-1]) 

plt.xlabel('$Input size (n)$')
plt.ylabel('$time (ms)$')
plt.title('Factorial of Number')
plt.plot(n1, t1,linewidth=2.0)
plt.plot(n1, t2,linewidth=3.0)


plt.show()

import time
import matplotlib.pyplot as plt


fact = 1
N=[]
for i in range(1,400,2):
  N.append(i)

# Factorial Iterative method
start=time.time()
t1=[]
for i in N:
  for j in range(1,i):
      fact*=j
  stop = time.time()
  t1.append(stop-start)

#Pure recursion
t2=[]
def fact0(n):
  if(n<1):
    return 1
  return n*fact0(n-1)
start = time.time()
for i in N:
  fact0(i)
  stop = time.time()
  t2.append(stop-start)

# Factorial using DP without recursion
t3=[]
ans=[]
start2 = time.time()
for i in N:
  fact*=i
  if fact in ans:
    fact= ans[ans.index(ans)]*i
    ans.append(fact)
  else:
    ans.append(fact)
  stop = time.time()
  t3.append(stop-start)

#Visualization
plt.xlabel('$Input size (n)$')
plt.ylabel('$time (ms)$')
plt.title('Factorial of Number')
plt.plot(N, t1,linewidth=2.0)
plt.plot(N, t2,linewidth=3.0)
plt.plot(N, t3,linewidth=4.0)

plt.show()

import time
import matplotlib.pyplot as plt


def inputN(n):
  N=[]
  for i in range(1,n,2):
    N.append(i)
  return N

# Factorial Iterative method
def fiterative(N):
  start=time.time()
  fact = 1
  t1=[]
  for i in N:
    for j in range(1,i):
      fact*=j
    stop = time.time()
    t1.append(stop-start)
  return t1

#Pure recursion

def fact0(n):
  if(n<1):
    return 1
  return n*fact0(n-1)

def frecurence(N):
  t2=[]
  start = time.time()
  for i in N:
    fact0(i)
    stop = time.time()
    t2.append(stop-start)
  return t2

# Factorial using DP without recursion
def fdp(N):
  t3=[]
  ans=[]
  fact = 1
  start2 = time.time()
  for i in N:
    fact*=i
    if fact in ans:
      fact= ans[ans.index(ans)]*i
      ans.append(fact)
    else:
      ans.append(fact)
    stop = time.time()
    t3.append(stop-start)
  return t3

# def inputN(n):
# def fiterative(N):
# def frecurence(N):
# def fdp(N):

N= inputN(200)
#print(N)
t1 = fiterative(N)
#print(t1)
t2 = frecurence(N)
t3 = fdp(N)

#Visualization
plt.xlabel('$Input size (n)$')
plt.ylabel('$time (ms)$')
plt.title('Factorial of Number')
plt.plot(N, t1,linewidth=2.0)
plt.plot(N, t2,linewidth=3.0)
plt.plot(N, t3,linewidth=4.0)

plt.show()