segundos_entrada = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos_entrada // 86400
resto_segs_dias = segundos_entrada % 86400
horas = resto_segs_dias // 3600
resto_segs_min = resto_segs_dias % 3600
minutos = resto_segs_min // 60
segundos = resto_segs_min % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
