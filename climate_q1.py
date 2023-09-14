import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

query = 'SELECT Year, CO2, Temperature FROM climate'
cursor.execute(query)

rows = cursor.fetchall()


years = []
co2 = []
temp = []


for row in rows:
    year, co2_value, temp_value = row[:3]
    years.append(year)
    co2.append(co2_value)
    temp.append(temp_value)

conn.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png")

