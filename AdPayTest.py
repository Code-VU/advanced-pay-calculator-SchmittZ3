hrs = input("Enter Hours:")
rate = input("Enter Pay Rate:")
hrs = float(hrs)
rate = float(rate)
if hrs > 40 :
    regpay = hrs*rate
    otpay = (hrs - 40.0) * (.5 * rate)
    pay = regpay + otpay
else:
    pay = hrs*rate
print("Pay: ",pay)