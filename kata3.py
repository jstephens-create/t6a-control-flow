# pick one

# A: Location Codes (nested loop). Print the codes for 3 aisles × 4 shelves, one row per aisle.
# Expected first row: A1-S1 A1-S2 A1-S3 A1-S4


# B: Incident Validation (guard clauses). Using the incidents in kata3.py, skip any with no branch or a severity outside 1–3, and print why.
# Expected: INC-1001 and INC-1004 are logged; INC-1002 and INC-1003 are skipped.

# Stretch: do the other Kata 3 option too.

total_aisles = 5
shelves_per_aisle = 4

for aisle in range(1, total_aisles + 1):
    for shelf in range(1, shelves_per_aisle + 1):
        print(f"A{aisle}-S{shelf}", end=" ")
    print()