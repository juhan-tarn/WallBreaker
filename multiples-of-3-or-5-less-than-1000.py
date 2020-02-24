'''
This function calculates the sum that is less than 1000, 
and the sum contains numbers that are multiples of 3 or 5 

And the total sum under this definition is 998 where the sum is less than 1000
'''
def sum_of_3_or_5_less_than_1000():
    total_sum, num = 0, 0
    while (total_sum + num) < 1000:
        num += 1
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num
    print(total_sum) #total_sum = 998

    
'''
This function calculates the sum by adding up multiples of 3 or 5 that are smaller than 1000
The total sum under this definition is 233168 where the numbers are multiples of 3 or 5 
and they are less than 1000
'''
def sum_of_3_or_5_less_than_1000_II():
    total_sum = 0
    for num in range(0, 1000):
        if (num % 3 == 0 or num % 5 == 0):
            total_sum = total_sum + num
    print(total_sum) # total_sum = 233168


'''
The reason I have written two solutions is that I'm not certain with the definition of the given problem 
as there are some ambiguities. Therefore, based on the question given, I wrote two possible solutions 
according to my interpretations of the problem. 
'''