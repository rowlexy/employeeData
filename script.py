import csv
from helper import healthFilter

with open("EmployeeData.csv") as healthData:
    reader = csv.DictReader(healthData)
    medicals = list(reader)
    results = healthFilter(medicals, BusinessTravel="Travel_Frequently", MaritalStatus="Single", OverTime="No", JobSatisfaction="4", Age_lte=30)
    
# print(results)

with open("Medicals.csv", "w", newline="") as medical_csv:
    writer = csv.DictWriter(medical_csv, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)
    