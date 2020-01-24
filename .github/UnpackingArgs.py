def health_calculator(age, apples, cigs):
    answer = (100-age) + (apples * 3.5) - (cigs * 2)
    print(answer)

buckys_data = [27, 20, 0]

health_calculator(buckys_data[0], buckys_data[1], buckys_data[2]) #Unpacks all
health_calculator(*buckys_data) #Same