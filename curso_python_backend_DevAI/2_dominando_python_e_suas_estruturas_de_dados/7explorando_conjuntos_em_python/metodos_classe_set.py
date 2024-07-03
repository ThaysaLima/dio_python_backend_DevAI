# Continuaçãp da Aula 01

#MÉTODOS DA CLASSE SET 

# 1) {}.union, junção dos dois conjuntos

conj_a = {1,2,3,4}
conj_b = {4,5,6,7}

resultado = conj_a.union(conj_b)
print(resultado) # {1, 2, 3, 4, 5, 6, 7}

# 2) {}.itersection, interseção dos dois conjuntos

conj_c = {1,2,3}
conj_d = {2,3,4}

resultado2 = conj_c.intersection(conj_d)
print(resultado2) # {2, 3}

# 3) {}.difference, diferença dos conjuntos

conj_e = {1,2,3}
conj_f = {2,3,4}

#diferença do conjunto f para o conjunto e
resultado3 = conj_e.difference(conj_f)
print(resultado3) # {1}

#diferença do conjunto e para o conjunto f
resultado4 = conj_f.difference(conj_e)
print(resultado4) # {4}

# 4) {}.symetric_difference, junção dos dois que não tem na união dos conjuntos 

conj_g = {1,2,3}
conj_h = {2,3,4}

resultado5 = conj_g.symmetric_difference(conj_h)
print(resultado5) # {1, 4}

# 5) {}.issubset, se um conjunto pertence ao outro. O retorno será em booleano 

conj_i = {1,2,3,4,5,6}
conj_j = {4,5,6}

resultado6 = conj_i.issubset(conj_j)
print(resultado6) # True

resultado7 = conj_j.issubset(conj_i)
print(resultado7) # False

# 6) {}.issuperset, se os elementos então dentro do outro conjunto. 

conj_k = {1, 2, 3}
conj_l = {4, 1, 2, 5, 6, 3}

#o todos os elementos do conj_l está dentro dos elementos do conj_k
resultado8 = conj_k.issuperset(conj_l)  
print(resultado8) # False

#o todos os elementos do conj_k está dentro dos elementos do conj_l
resultado9 = conj_l.issuperset(conj_k)  
print(resultado9) # True

# 7) {}.isdisjoint, vai relacionar se os números tem alguma coincidência dentro dos conjuntos em si. 

conj_m = {1,2,3,4,5}
conj_n = {6,7,8,9}

conj_o = {1,0} 

# o conjunto n NÃO tem NADA relacionado com o conjunto m 
resultado10 = conj_m.isdisjoint(conj_n)
print(resultado10) #TRUE

# o conjunto o tem um item 1 igual ao conjunto m, logo ele está relacionado
resultado11 = conj_m.isdisjoint(conj_o)
print(resultado11) #FALSE

