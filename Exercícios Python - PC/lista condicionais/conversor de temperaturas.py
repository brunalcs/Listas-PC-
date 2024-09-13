if escala == "C":
    # celsius
    c = float(temp)
    # farennheit
    f = (9 / 5 * c) + 32
    # kelvin
    k = c + 273.15
    print(f"Temperatura em Celsius: {c:.2f} °C")
    print(f"Temperatura em Fahrenheit: {f:.2f} °F")
    print(f"Temperatura em Kelvin: {k:.2f} K")
elif escala == "F":
    f = float(temp)
    c = 5 / 9 * (f - 32)
    k = c + 273.15
    print(f"Temperatura em Celsius: {c:.2f} °C")
    print(f"Temperatura em Fahrenheit: {f:.2f} °F")
    print(f"Temperatura em Kelvin: {k:.2f} K")
elif escala == "K":
    k = float(temp)
    c = k - 273.15
    f = (9 / 5 * c) + 32
    print(f"Temperatura em Celsius: {c:.2f} °C")
    print(f"Temperatura em Fahrenheit: {f:.2f} °F")
    print(f"Temperatura em Kelvin: {k:.2f} K")

