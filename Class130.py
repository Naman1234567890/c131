import csv

rows = []

with open("main.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
planet_data_rows = rows[1:]
print(headers)
print(planet_data_rows[0])


headers[0] = "row_num"

solar_system_planet_count = {}
for planet_data in planet_data_rows:
  if solar_system_planet_count.get(planet_data[11]):
    solar_system_planet_count[planet_data[11]] += 1
  else:
    solar_system_planet_count[planet_data[11]] = 1

max_solar_system = max(solar_system_planet_count, key=solar_system_planet_count.get)
print("Solar system {} has maximum planets {} out of all the solar systems we have discovered so far!".format(max_solar_system, solar_system_planet_count[max_solar_system]))



# print(maxssp)
# print("#########")
# print(spc)
hd_10180_planets=[]
for planet_data in planet_data_rows:
    if max_solar_system==planet_data[11]:
        hd_10180_planets.append(planet_data)
print(len(hd_10180_planets))




