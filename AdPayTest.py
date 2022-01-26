try:
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Pay Rate:"))
except:
    print("Error, please enter numeric input"),quit()

if hrs > 40 :
    regpay = hrs*rate
    otpay = (hrs - 40.0) * (.5 * rate)
    pay = regpay + otpay
else:
    pay = hrs*rate
print("Pay:",pay)