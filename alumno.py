# Obtener el total que tendrá que pagar un alumno si la colegiatura para alumnos de profesional es de $300 por cada cinco unidades y para alumnos de preparatoria es de $180 por cada cinco unidades, de acuerdo a los siguientes criterios:
# Si el promedio es de 9.5 o más y el alumno es de preparatoria, entonces este podrá cursar 55 unidades y se le hará un 25% de descuento.
# Si el promedio es mayor o igual a 9 pero menor que 9.5 y el alumno es de preparatoria, entonces este podrá cursar 50 unidades y se le hará un 10% de descuento.
# Si el promedio es mayor que 7 y menor que 9 y el alumno es de preparatoria, este podrá cursar 50 unidades y no tendrá ningún descuento.
# Si el promedio es de 7 o menor, el número de materias reprobadas es de 0 a 3 y el alumno es de preparatoria, entonces podrá cursar 45 unidades y no tendrá descuento.
# Si el promedio es de 7 o menor, el número de materias reprobadas es de 4 o más y el alumno es de preparatoria, entonces podrá cursar 40 unidades y no tendrá ningún descuento.
# Si el promedio es mayor o igual a 9.5 y el alumno es de profesional, entonces podrá cursar 55 unidades y se le hará un 20% de descuento.
# Si el promedio es menor de 9.5 y el alumno es de profesional, entonces podrá cursar 55 unidades y no tendrá descuento.

alumnno = input("Ingrese el tipo de alumno (preparatoria/profesional): ")
if alumnno.lower() == "preparatoria":
    promedio = float(input("Ingrese el promedio del alumno: "))
    if promedio >= 9.5:
        unidades = 55
        descuento = 0.25
    elif promedio >= 9 and promedio < 9.5:
        unidades = 50
        descuento = 0.10
    elif promedio > 7 and promedio < 9:
        unidades = 50
        descuento = 0
    else:
        materias_reprobadas = int(input("Ingrese el número de materias reprobadas: "))
        if materias_reprobadas <= 3:
            unidades = 45
            descuento = 0
        else:
            unidades = 40
            descuento = 0

    costo_unitario = 180 / 5
    costo_total = unidades * costo_unitario * (1 - descuento)
    print(f"El alumno podrá cursar {unidades} unidades y deberá pagar un total de ${costo_total:.2f}")
else:
    promedio = float(input("Ingrese el promedio del alumno: "))
    if promedio >= 9.5:
        unidades = 55
        descuento = 0.20
    else:
        unidades = 55
        descuento = 0

    costo_unitario = 300 / 5
    costo_total = unidades * costo_unitario * (1 - descuento)
    print(f"El alumno podrá cursar {unidades} unidades y deberá pagar un total de ${costo_total:.2f}")