#FEITO EM HOMENAGEM AO GRANDE LUCAS MENEZES FAMOSO CR QUE TEM NECESSIDADE IMEDIATA DE SABER SEUS RESULTADOS AO VIVO

em330 = {
    "nome": "EM330 - Oficinas",
    "cred": 4
}
em360 = {
    "nome": "EM360 - Termodinamica I",
    "cred": 4
}
f428 = {
    "nome": "F428 - Fisica Geral IV",
    "cred": 4
}
ma311 = {
    "nome": "MA311 - Calculo III",
    "cred": 6
}
mc102 = {
    "nome": "MC102 - Algoritimos",
    "cred": 6
}
em335 = {
    "nome": "EM335 - Tecnologia Mecanica",
    "cred": 4
}
f329 = {
    "nome": "F329 - Fisica Experimental III",
    "cred": 2
}
credt = 0
soma = 0
tsem = [em330, f329, em335, mc102, ma311, f428, em360]
for i in range(0,len(tsem)):
    print(tsem[i]["cred"], tsem[i]["nome"])
for j in range(0, len(tsem)):
    print("Sua nota de ",tsem[j]["nome"])    
    var = float(input())
    soma = float(soma + var*tsem[j]["cred"])
for k in range(0, len(tsem)):
    credt += tsem[k]["cred"]
op = float(soma/credt)
print("Seu CR atual e: ", op)
