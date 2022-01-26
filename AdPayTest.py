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