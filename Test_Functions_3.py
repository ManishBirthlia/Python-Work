from tkinter import N


def natural_number_sum(n):
    for i in range (1,n):
       n=i+n
    return n

print(f'the sum upto given no. is {natural_number_sum(6)}')