#Use python lists and make an list of numbers.
list = [0,1,2,3,4,5,6,7,8,9]
#Write a function which returns sum of the list of numbers
def sumOfListElements(list):
   sum=0;
   for i in range(0,len(list)):
    sum+=list[i]
   return sum

print(sumOfListElements(list)) 
