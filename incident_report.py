# incident_report.py - T7A starter
# Calculates downtime totals for warehouse incidents (Operations Problem Navigator).
# Heads up: this code is repetitive AND has bugs. That's on purpose.
 
north_dc = [45, 30, 120, 15]   # downtime minutes per incident
west_dc = [90, 20, 45]         # downtime minutes per incident
south_dc = [60, 10, 25]        # downtime minutes per incident
east_dc = [60, 10, 25]         # downtime minutes per incident
 
def calculate_total(minutes_list):
    total = 0
    for m in minutes_list:
        total = total + m
    return total

# Counts incidents longer than 60 minutes in a list.

def count_major_incidents(minutes_list):
    count = 0
    for m in minutes_list:
        if m >= 60:
            count = count + 1
    return count

print("North DC total downtime:", calculate_total(north_dc))
print("West DC total downtime:", calculate_total(west_dc))
print("South DC total downtime:", calculate_total(south_dc))
print("East DC total downtime:", calculate_total(east_dc))

print("North DC major incidents (over 60 min):", count_major_incidents(north_dc))
print("West DC major incidents (over 60 min):", count_major_incidents(west_dc))
print("East DC major incidents (over 60 min):", count_major_incidents(east_dc))
print("South DC major incidents (over 60 min):", count_major_incidents(south_dc))

# FIXED: IndexError on the next line.
# Hypothesis: north_dc has 4 items, so the highest index is 3.
# Evidence: print(len(north_dc)) showed 4. Index 4 does not exist.
# Fix: use north_dc[-1] to get the last item. Index -1 counts from the end.

print("Most recent North DC incident:", north_dc[-1])
 


raw = input("Log a new North DC incident (minutes): ")

# Fix: wrapped int(raw) in try/except ValueError so letters don't crash it.
# Moved append and the total print inside try so they only run when int(raw) works.
# BUG: NameError on the line north_dc.append(new_minutes).
# Hypothesis: since int(raw) crashed, new_minutes was never defined, and was later called
# Evidence: NameError - new_minutes was not assigned a value

try:
    new_minutes = int(raw)
    north_dc.append(new_minutes)
    print("New North DC total:", sum(north_dc))
except ValueError:
    print("Please enter a whole number, like 30.")

