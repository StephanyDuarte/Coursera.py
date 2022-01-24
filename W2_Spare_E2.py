
Tempo = int(input("Por favor, entre com o número de segundos que deseja converter:"))

a = Tempo // (24*3600)
T_aux_horas = Tempo % (24*3600)
b = T_aux_horas // 3600
c = (T_aux_horas % 3600) // 60
d = ((T_aux_horas % 3600) % 60)

print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos.")
