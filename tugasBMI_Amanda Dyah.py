weight = float(input("Masukkan berat (kg): "))
height = float(input("Masukkan tinggi (m): "))

bmi = weight / height ** 2

print("BMI anda adalah " + str(bmi))

if bmi < 18.5:
    print("Underweight")
elif bmi < 23:
    print("Normal Weight")
elif bmi < 25:
    print("Overweight")
elif bmi > 30:
    print("Obesity class I")
else:
    print("Obesity class II")