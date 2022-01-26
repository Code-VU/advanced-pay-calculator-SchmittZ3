def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    try:
        hrs = float(hrs)
    except:
        print("Error, please enter numeric input")
        exit()
    rate = input("Enter Pay Rate:")
    try:
        rate = float(rate)
    except:
        print("Error, please enter numeric input")
        exit()
    if hrs > 40 :
        regpay = hrs*rate
        otpay = (hrs - 40.0) * (.5 * rate)
        pay = regpay + otpay
    else:
        pay = hrs*rate
    print("Pay:",pay)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()