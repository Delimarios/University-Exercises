n=(int(input("Enter the degree of the polynomial (n>0): ")))
while n<0:
    n=int(input("Enter a Non-Negative Number: "))

coeffs=[]
for i in range(n+1):
    c=int(input(f"Enter the coefficient of x^{i}: "))
    coeffs.append(c)

deriv_coeffs=[coeffs[i] *i  for i in range(1,len(coeffs))]

deriv_term=[]
for i in range(len(deriv_coeffs)):
    if deriv_coeffs[i]==0:
        continue
    if i==0:
        deriv_term.append(str(deriv_coeffs[i]))
    elif i==1:
        deriv_term.append(str(deriv_coeffs[i]) + "x")
    else:
        deriv_term.append(str(deriv_coeffs[i]) + "x^" + str(i))

print(f"f´(x)= " + "+".join(deriv_term))


if n==3 and deriv_coeffs[2]!=0:
   a=deriv_coeffs[2]
   b=deriv_coeffs[1]
   c=deriv_coeffs[0]
   D=b*b-4*a*c
   print(f"D= {D}")


   if D >0:
       sqrD = D *0.5
       x1 = (-b + sqrD) / (2 * a)
       x2 = (-b - sqrD) / (2 * a)
       print(f"f´(x) has two Roots x1: {x1}, and x2 {x2}")
   elif D==0:
       x0=-b/(2*a)
       print(f"Double root of f'(x): {x0}")
   else:
       print("f'(x) has no real roots.")













