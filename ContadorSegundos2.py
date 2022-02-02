#Converte "segundos" em "dias, horas, minutos e segundos"

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
segs_restantes_dias = segundos % 86400
horas = segs_restantes_dias // 3600
segs_restantes_horas = segs_restantes_dias % 3600
minutos = segs_restantes_horas // 60
segs_restantes_min = segs_restantes_horas % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs_restantes_min,"segundos.")
