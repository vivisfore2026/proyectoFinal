
H_trabajadas=float(input("Digite numero de horas"))

if H_trabajadas>0 and H_trabajadas < 135 :
    if H_trabajadas <= 40 :
        print("No realizo horas extras en la semana")
        salario= 1600 * H_trabajadas

    else:
        print("Realizo horas extras:")
        H_extras= H_trabajadas - 40
        V_extras= H_extras*2000
        print("Usted laboro ", H_extras, " horas extras.")
        print("El valor a pagar por horas extras es: ",V_extras)
        V_normal=40*1600
        print("Su salario basico es: ",V_normal)
        salario=V_extras + V_normal

    print("Su salario semanal es ",salario)

else:
    print("La cantidad de horas debe ser mayor a 0 y menor que 135")