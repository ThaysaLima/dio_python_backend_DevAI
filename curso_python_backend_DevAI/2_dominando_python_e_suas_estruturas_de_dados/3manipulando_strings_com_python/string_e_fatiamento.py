# Aula 01
nome = "THaYsa"

print(nome.upper()) # THAYSA
print(nome.lower()) # thaysa
print(nome.title()) # Thaysa

texto = "  Olá, mundo!   "
print(texto)
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu = "Python"

print("###" + menu + "###") # 12 caracteres  = quero deixa desse jeito. 
print(menu.center(12))
print(menu.center(12, "#"))