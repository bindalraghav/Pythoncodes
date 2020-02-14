def odd_even(l):
    odd_nums=[]
    even_nums=[]
    filt_nums=[odd_nums,even_nums]
    for i in l:
        if i%2==0:
             even_nums.append(i)
        else:
            odd_nums.append(i)

    return filt_nums

nums=list(range(1,11))
print(odd_even(nums))
