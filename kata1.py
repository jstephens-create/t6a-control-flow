# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start

for check in range(2, 11):
    minutes = check * 15
    print(f"Check {check}: {minutes} minutes after shift start")