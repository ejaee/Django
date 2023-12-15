import pyotp

# OTP 생성
totp = pyotp.TOTP('JBSWY3DPEHPK3PXP')

# OTP 출력
print("Current OTP:", totp.now())

# OTP 검증
otp = input("Enter OTP:")
result = totp.verify(otp)
if result:
    print("OTP verified successfully.")
else:
    print("Invalid OTP.")