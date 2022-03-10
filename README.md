# QOSF_Mentorship_Application

### Updates: 
  1. I got accepted to the mentorship, you can (soon) take a look at all the projects (including mine) from this Cohort 4 [here](https://qosf.org/mentorship_cohort_4/).

  2. My solution got selected as a "Model Solution".

![](screenshot.png)

Maybe my solution can help future applicants or anyone who might want to solve this problem. So, on my next update I'm going to fix some typos (mostly grammar) and correct a small circuit draw.

---

3. The problem we were required to solve:
  
  * Design a quantum circuit that considers as input the following vector of integers numbers: [1,5,7,10]

* Returns a quantum state which is a superposition of indices of the target solution, obtaining in the output the indices of the inputs where two adjacent bits will always have different values. In this case the output should be: (|01> + |11>)/sqrt{2} , as the correct indices are 1 and 3.

- 1 = 0001
- **5 = 0101**
- 7 = 0111
- **10 = 1010**

* Bonus: Design a general circuit that accepts vectors with random values of size 2^n with m bits in length for each element and finds the state(s) indicated above from an oracle.

* Observation - the input vector:
1) Doesn't have repeated integers.
2) Always have two solutions.


End of updates.

---
#### Dear evaluator,

My main solution is on the jupyter notebook Task1_Lucas_Arenstein.ipynb .
I think this is the fastest way to grade my solution.

But if you don't want to use jupyter and just want to read my report you could go to Task1_Lucas_Arenstein.html

To run the code in a terminal for the task 1 just type:

python3 Task1_Bonus_Solution1.py [1,5,7,10]

and to run the script with any input you desire (bonus part) just run:

python3 Task1_Bonus_Solution1.py [1,2,3,...,2^n] 

if you want to try the Solution 2 run: python3 Task1_Bonus_Solution2.py [1,2,3,...,2^n] on the terminal.

And finally you can run this codes in a IDE, using this option you will see the expected answer and the histograms aswell.
running the function sol1_bonus([1,2,3,4...]).


#### Thank you for your time and opportunity :)
#### Lucas
