print("Percentual de votos da eleição")
v_t = int(input("Digite quantos votos totais: "))
v_b = int(input("Quantos votos brancos? "))
v_n = int(input("E votos nulos?"))
v_v = int(input("E os válidos?"))
Pv_b = v_b*100/v_t
Pv_n = v_n*100/v_t
Pv_v = v_v*100/v_t
print("Dos", v_t, "votos totais, "+ str(Pv_b)+ "% foram brancos", Pv_n, "% nulos", "e", Pv_v, "% de votos válidos")