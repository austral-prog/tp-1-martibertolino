def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    horacompletas=(total_segundos//3600)
    print(horacompletas)
    minutoscomp=((total_segundos%3600)//60)
    print(minutoscomp)
    segundosrest=(((total_segundos%3600)%6))
    print(segundosrest)
