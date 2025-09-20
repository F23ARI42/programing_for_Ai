
employees = {
    "Alice": {"tasks_completed": [1, 2, 1.5], "department": "HR"},
    "Bob": {"tasks_completed": [3, 4, 5], "department": "IT"},
    "Charlie": {"tasks_completed": [2, 2, 2], "department": "Finance"},
    "Diana": {"tasks_completed": [1, 1, 1], "department": "HR"},
    "Eve": {"tasks_completed": [5, 6, 7], "department": "IT"}
}
employee_avg_times = {}
for emp, data in employees.items():
    tasks = data["tasks_completed"]
    avg_time = sum(tasks) / len(tasks)
    employee_avg_times[emp] = avg_time
performance_categories = {"Excellent": [], "Good": [], "Needs Improvement": []}
for emp, avg_time in employee_avg_times.items():
    if avg_time <= 2:
        performance_categories["Excellent"].append(emp)
    elif 2 < avg_time <= 4:
        performance_categories["Good"].append(emp)
    else:
        performance_categories["Needs Improvement"].append(emp)
department_performance = {}
for emp, data in employees.items():
    dept = data["department"]
    if dept not in department_performance:
        department_performance[dept] = {"Excellent": 0, "Total": 0}
    if emp in performance_categories["Excellent"]:
        department_performance[dept]["Excellent"] += 1
    department_performance[dept]["Total"] += 1
best_dept = None
highest_percentage = 0
for dept, stats in department_performance.items():
    if stats["Total"] > 0:
        percentage = (stats["Excellent"] / stats["Total"]) * 100
        if percentage > highest_percentage:
            highest_percentage = percentage
            best_dept = dept
slowest_employee = max(employee_avg_times, key=lambda x: employee_avg_times[x])
print("Employee Average Times:", employee_avg_times)
print("Performance Categories:", performance_categories)
print("Best Performing Department:", best_dept)
print("Slowest Employee:", slowest_employee)