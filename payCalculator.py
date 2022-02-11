def calculatePay():
    
    # This first line is provided for you
hrs = input("Enter Hours: ")

try:
    float(hrs)
    try:
        rate = input("Enter Pay Rate:")
        float(rate)
        if float(hrs) > 40 :
            regpay = 40 * float(rate)
            otpay = (float(hrs) - 40.0) * (float(rate)*1.5)
            pay = regpay + otpay
        else:
            pay = float(hrs) * float(rate)
        print("Pay:",pay)
    except:
        print("Error, please enter numeric input")
except:
    print("Error, please enter numeric input")
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()