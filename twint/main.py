
import twint


# Configurar la búsqueda

c = twint.Config()
print("Introduce porfa una cuenta de Twitter: \t")
c.Username = input()
print("Quieres buscar una palabra?: Si no es asi mostraremos los ultimos tweets. [y/n]\t")
n = input()
if n != '':
    c.Search = n 

# Correr la búsqueda

twint.run.Search(c)

