# Aula 06 

frutas = ["limão", "uva"]
print("laranja" in frutas) #>>> False

#Key Sensitive

cidades = ["Fortaleza", "Aracati", "Maracanau"]

print("fortaleza" in cidades) #>>> False, pois quando foi feito a comparação não colocamos Fortaleza com F maiúsculo. 


print("Cidade" not in cidades) #>>> True, pois ele realmente não está na lista. 