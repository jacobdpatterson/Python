def get_gender(sex='Unknown'):
    if sex == 'm':
        sex = "Male"
    elif sex == 'f':
        sex = "Female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()