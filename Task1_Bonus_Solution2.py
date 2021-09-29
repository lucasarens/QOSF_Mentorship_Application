#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import numpy as np, math
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

def initial_state(in_vector):
    
    #Check and get n
    n = len(in_vector)
    if n%2 != 0:
        print('Invalid Input - Vector must have size 2^n, with n>=2')
        return 0,0,0
    else: n = int(math.log(len(in_vector),2))
        
    #Find m
    m = len(np.binary_repr(max(in_vector)))
    
    #Binary vector with binary indices
    bi_vector_bi_index = [0]* 2**n
    
    #This vector will contain the integer values of the indices 
    #from the bi_vector_bi_index
    index_vector = [0]* 2**n

    for i in range(len(in_vector)):
        bi_vector_bi_index[i] = (str(np.binary_repr(in_vector[i],m)) + str(np.binary_repr(i,n)))
        index_vector[i] = int(bi_vector_bi_index[i],2)
 
    initial_state_vector = [0] * 2**(n+m)
    
    #Fill the initial_state_vector with amplitudes that respect
    #the normalization condition for each of the states of ket{psi}
    for i in index_vector:
        initial_state_vector[i] = 1/math.sqrt(len(index_vector))

    return initial_state_vector, n, m

def target_state(n,m):
    # For the "Oracle" part we need to generate s_1 and s_2
    s1 = ['0']*(m)
    s2 = ['1']*(m)
    for i in range(1,m,2):
        s1[i] = '1'
        s2[i] = '0'

    #0101...00    
    first_index_s1 = int((''.join(s1) + ''.join(['0']*n)),2)
    #1010...00
    first_index_s2 = int((''.join(s2) + ''.join(['0']*n)),2)
    
    #Calculating the index of each one of the state of \ket{\psi_t} 
    l_index = [0]*2**(n+1)
    l_index[0] = first_index_s1
    l_index[2**n] = first_index_s2
    
    #first half: |s_1 00..00> |s_1 00..01>,..., |s_1 11..111>
    #second half: |s_2 00..00> |s_2 00..01>,..., |s_2 11..111>
    for i in range(1,2**n):
        l_index[i] = l_index[i-1] + 1
        l_index[i+2**n] =l_index[(i-1)+2**n] + 1
    
    psi_t = [0] * 2 **(m+n)
    
    for i in l_index:
        psi_t[i] = 1/math.sqrt(len(l_index))
    
    return psi_t


def build_reflection(vector):
    row = np.array(vector)
    col = row.transpose()
    #Identity matrix with the appropriate size
    S = (2*(np.outer(col,row))) - np.identity(len(vector))
    
    return S


def printb(n):
    for i in range(2**n):
        print(i, '-', np.binary_repr(i,n))
    
    return



def sol2_bonus(input_vector):
    in_vector = list(input_vector)
    
    psi_i, n, m = initial_state(in_vector)
    if n == 0:
        return 
    
    psi_t = target_state(n,m)
    
    #Building S_i and S_t and calculate R
    S_i = build_reflection(psi_i)
    
    S_t = build_reflection(psi_t)
    
    R = - np.matmul(S_t,S_i)
    
    qc = QuantumCircuit(n+m,n)
    
    qc.initialize(psi_i, list(range(m+n)))
    
    #Number of iterations to apply R onto \ket{\psi_i}
    for i in range(2**n):
        qc.unitary(R, list(range(m+n)), label='R')
    
    for i in range(n):
        qc.measure(i,i)
    
    backend = Aer.get_backend('statevector_simulator')
    results = execute(qc,backend).result().get_counts()

    #Plot just the desired amplitudes
    for i in range(0,(2**n - 2)):
        min_key = min(results.keys(), key=lambda k: results[k]) 
        del results[min_key]
    #To see all the amplitudes - just comment (#) in the for loop above
    
    print("Solution for the input:", input_vector)
    
    answer = list(results.keys())
    
    print('1/sqrt(2) * (|',answer[0],'> + |',answer[1],'>)')


    return plot_histogram(results)

#To run using a IDE
#just run everything from line 1 to here everything and call the function
#with your desired input
#> sol2_bonus([1,2,3,4...])



#To run in the terminal
#python3 Task1_Bonus_Solution2.py [1,2,3,4,...]
if __name__ == "__main__":
    in_vector = sys.argv[1]
    l = list(map(int, in_vector.strip('[]').split(',')))
    sol2_bonus(l)
    
    
    
    
