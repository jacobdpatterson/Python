item = ['Crumb', 'Bum', 'Scum']
print(item[0])

crumbholder, bumholder, scumholder = ['Crumb', 'Bum', 'Scum']
print(crumbholder)

def drop_first_last(grades):
    first, *middle, last = grades # Take first, all in middle, and last.
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([50,60,70,80,90])
drop_first_last([50, 60, 70, 80, 90, 95, 99, 100, 101])