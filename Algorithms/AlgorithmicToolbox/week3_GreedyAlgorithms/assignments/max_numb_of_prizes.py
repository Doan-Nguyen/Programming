input_value = int(input())
#
count = 0
while(input_value > input_value/2):
    for i in range(1, input_value/2):
        input_value -= i
    if input_value