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
print(resultado10) #TRUE, para chegar ao TRUE não pode haver semelhantes entre os conjuntos.

# o conjunto o tem um item 1 igual ao conjunto m, logo ele está relacionado
resultado11 = conj_m.isdisjoint(conj_o)
print(resultado11) #FALSE

# 8) {}.add, adiciona um elemento se ele já não tiver no conjunto

conj_p = {1,2,3}
conj_p.add(4)
print(conj_p) # {1, 2, 3, 4}

# 9) {}.copy, cria uma cópia nova, onde essa nova cópia não interfere na original 

conj_q = {1,2,3} # conjunto original

copia_q = conj_q.copy()
lista_copia_q = list(copia_q)
lista_copia_q[1] = 6

print(conj_q) # {1, 2, 3}
print(lista_copia_q) # [1, 6, 3]

# 10) {}.discard, vai descartar o item que for indicado

conj_r = {1,2,4,5}
conj_r.discard(2) 
print(conj_r) # {1, 4, 5}

# 11) {}.pop, remove um item na posição fornecida (primeiro transformar em lista) e retorna. Se não for indicado o item ele irá remover o primeiro da lista. 

conj_s = {1,2,3,4,5,6,7,8,9,10}

print(conj_s.pop()) # 1
print(conj_s) # {2,3,4,5,6,7,8,9,10}

#para remover um item específico eu posso: 
#1 fazer uma cópia, 2 transformar esse cópia em lista, 3 acessar o item específico para remover através do index. 

copia_conj_s = conj_s.copy()
lista_copia_conj_s = list(conj_s)

                            #3 = index
print(lista_copia_conj_s.pop(3)) #5
print(lista_copia_conj_s) # [2, 3, 4, 6, 7, 8, 9, 10]

# 12) {}.remove, remove um item da lista. 

conj_t = {3,6,9,12}
conj_t.remove(6)
print(conj_t) # {9, 3, 12}, ele não retorna em uma ordem. 

# 13) len(), mostra o comprimento

conj_w = {2,4,6,8,10,12,14,16,18}
print(len(conj_w)) # 9

# 14) in(), verifica se o item pedido está na lista. 

conj_x = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}

print(1 in conj_x) #TRUE
print(34 in conj_x) #FALSE 


