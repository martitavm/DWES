temperaturas_celsius =  [0, 10, 20, 30, 40]
# [ F = C \times \frac{9}{5} + 32 ]

temperaturas_fahrenheit = list(map(lambda calcula_temperatura: calcula_temperatura * 9/5 +32, temperaturas_celsius ))
print(temperaturas_fahrenheit)