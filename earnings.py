import math

def tim():

    tim_earnings = []
    for x in range(12):
        tim = input("Tims Earnings: ")
        tim_earnings.append(tim)
    return tim_earnings


def sara():

    sara_earnings = []
    for x in range(12):
        sara = input("Sara's Earnings: ")
        sara_earnings.append(sara)
    return sara_earnings


def total():
    
    tim_earnings = tim()
    sara_earnings = sara()
    for i in range(12):
        total_earnings = float(tim_earnings[i]) + float(sara_earnings[i])
        print(f"Total earnings for both in month {i+1}: {total_earnings}")
    
    
total()
