#[---------]
# QUESTION 3

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]

#create empty list in order to feed the numbers into
part3_answer = []

#used a foor loop to return and append the even numbers
for num in part3:
    
    if num % 2 == 0:
        part3_answer.append(num)


print('List of the even numbers: ', part3_answer)
