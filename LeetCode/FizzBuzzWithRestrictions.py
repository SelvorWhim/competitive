# note: this ugly little piece of code solves a code challenge to implement Fizz Buzz in Python for a single number, where the code must not contain if,==,!=,str,def,return,import,eval and exec. These restrictions are enforced in the tests.

fizz_buzz = lambda n: "".join([(n%3<=0)*"Fizz", (n%15<=0)*" ", (n%5<=0)*"Buzz", (n%3>0 and n%5>0)*"{}".format(n)])
