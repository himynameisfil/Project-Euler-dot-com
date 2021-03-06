#Status: Solved

#Problem : Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Solution : I am creating a fibonacci function that will determine the nth fibonacci number using the formula related to the golden ratio
goldenratio = (1 + 5**.5)/2
negagolden = ( 1- 5 ** .5)/2
def fibonacci(x):
  n = ((goldenratio ** x) - (negagolden ** x)) / (5 ** .5)
  return int(round(n,0))

#From this point on, I just run the function and all the outputs together until the function returns something over 4 million
count = 0
i = 0
while fibonacci(i)<4000000:
  if fibonacci(i)%2==0:
    count+=fibonacci(i)
  i+=1
print(count)
