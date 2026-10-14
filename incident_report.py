# incident_report.py - T7A starter
# Calculates downtime totals for warehouse incidents (Operations Problem Navigator).
# Heads up: this code is repetitive AND has bugs. That's on purpose.
 
north_dc = [45, 30, 120, 15]   # downtime minutes per incident
west_dc = [90, 20, 45]          # downtime minutes per incident
south_dc = [60, 10, 25]
east_dc = [60, 10, 25]
 
def calculate_total(minutes_list):
    total = 0
    for m in minutes_list:
        total = total + m
    return total

print("North DC total downtime:", calculate_total(north_dc))
print("West DC total downtime:", calculate_total(west_dc))
print("South DC total downtime:", calculate_total(south_dc))
print("East DC total downtime:", calculate_total(east_dc)) 
print(len(north_dc))

# BUG: IndexError on this line.
# Hypothesis: north_dc has 4 items, so the highest index is 3.
# Evidence: print(len(north_dc)) showed 4. Index 4 does not exist.

print("Most recent North DC incident:", north_dc[4])
 
new_minutes = int(input("Log a new North DC incident (minutes): "))
north_dc.append(new_minutes)
print("New North DC total:", sum(north_dc))

