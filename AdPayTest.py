hrs = input("Enter Hours: ")

try:
    hrs = float(hrs)
    try:
        rate = float(input("Enter Pay Rate:"))
        if hrs > 40 :
            regpay = hrs*rate
            otpay = (hrs - 40.0) * (.5 * rate)
            pay = regpay + otpay
        else:
            pay = hrs*rate
        print("Pay:",pay)
    except:
        print("Error, please enter numeric input")
except:
    print("Error, please enter numeric input")