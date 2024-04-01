from openpyxl import Workbook

# Create a new Excel workbook
wb = Workbook()

# Select the active worksheet
ws = wb.active

# Define the headers
ws.append(["PARENT_ID", "FIRST_NAME", "LAST_NAME", "PHONE_NO", "EMAIL_ADDRESS"])

# Generate some sample data
parent_data = [
    (10001, "Emily", "Johnson", 9876543210, "emily.johnson@example.com"),
    (10002, "Michael", "Smith", 8765432109, "michael.smith@example.com"),
    (10003, "Sophia", "Williams", 7654321098, "sophia.williams@example.com"),
    (10004, "Jacob", "Brown", 6543210987, "jacob.brown@example.com"),
    (10005, "Olivia", "Jones", 5432109876, "olivia.jones@example.com"),
    (10006, "Ethan", "Davis", 4321098765, "ethan.davis@example.com"),
    (10007, "Ava", "Miller", 3210987654, "ava.miller@example.com"),
    (10008, "Matthew", "Wilson", 2109876543, "matthew.wilson@example.com"),
    (10009, "Isabella", "Taylor", 1098765432, "isabella.taylor@example.com"),
    (10010, "William", "Anderson", 9988776655, "william.anderson@example.com"),
    (10011, "Mia", "Martinez", 8877665544, "mia.martinez@example.com"),
    (10012, "Alexander", "Thomas", 7766554433, "alexander.thomas@example.com"),
    (10013, "Charlotte", "Garcia", 6655443322, "charlotte.garcia@example.com"),
    (10014, "James", "Hernandez", 5544332211, "james.hernandez@example.com"),
    (10015, "Amelia", "Robinson", 4433221100, "amelia.robinson@example.com"),
    (10016, "Benjamin", "Young", 3322110099, "benjamin.young@example.com"),
    (10017, "Harper", "Rodriguez", 2211009988, "harper.rodriguez@example.com"),
    (10018, "Daniel", "Lewis", 1100998877, "daniel.lewis@example.com"),
    (10019, "Evelyn", "Hall", 9900887766, "evelyn.hall@example.com"),
    (10020, "Oliver", "Allen", 8798765432, "oliver.allen@example.com"),
    (10021, "Abigail", "Scott", 7687654321, "abigail.scott@example.com"),
    (10022, "Samuel", "King", 6576543210, "samuel.king@example.com"),
    (10023, "Elizabeth", "Adams", 5465432109, "elizabeth.adams@example.com"),
    (10024, "Henry", "Green", 4354321098, "henry.green@example.com"),
    (10025, "Sofia", "Baker", 3243210987, "sofia.baker@example.com"),
    (10026, "David", "Perez", 2132109876, "david.perez@example.com"),
    (10027, "Victoria", "Turner", 1021098765, "victoria.turner@example.com"),
    (10028, "Joseph", "Campbell", 9910987654, "joseph.campbell@example.com"),
    (10029, "Madison", "Mitchell", 8809876543, "madison.mitchell@example.com"),
    (10030, "Gabriel", "Hill", 7798765432, "gabriel.hill@example.com"),
    (10031, "Lily", "Ramirez", 6687654321, "lily.ramirez@example.com"),
    (10032, "Andrew", "Moore", 5576543210, "andrew.moore@example.com"),
    (10033, "Grace", "Clark", 4465432109, "grace.clark@example.com"),
    (10034, "Christopher", "Nelson", 3354321098, "christopher.nelson@example.com"),
    (10035, "Avery", "White", 2243210987, "avery.white@example.com"),
    (10036, "Dylan", "Carter", 1132109876, "dylan.carter@example.com"),
    (10037, "Scarlett", "Ward", 9921098765, "scarlett.ward@example.com"),
    (10038, "Ryan", "Morris", 9910098765, "ryan.morris@example.com"),
    (10039, "Chloe", "Watson", 8809987654, "chloe.watson@example.com"),
    (10040, "Jonathan", "Brooks", 7798876543, "jonathan.brooks@example.com"),
    (10041, "Penelope", "Bennett", 6688765432, "penelope.bennett@example.com"),
    (10042, "Nathan", "Wright", 5577654321, "nathan.wright@example.com"),
    (10043, "Zoe", "Morgan", 4466543210, "zoe.morgan@example.com"),
    (10044, "Julian", "Wood", 3355432109, "julian.wood@example.com"),
    (10045, "Hailey", "Russell", 2244321098, "hailey.russell@example.com"),
    (10046, "Cameron", "Griffin", 1133210987, "cameron.griffin@example.com"),
    (10047, "Natalie", "Diaz", 8822109876, "natalie.diaz@example.com"),
    (10048, "Eleanor", "Hayes", 9911098765, "eleanor.hayes@example.com"),
    (10049, "Connor", "Harrison", 8809987654, "connor.harrison@example.com"),
    (10050, "Leah", "Knight", 7798876543, "leah.knight@example.com")
]

# Add the sample data to the worksheet
for row in parent_data:
    ws.append(row)

# Save the workbook to a file
wb.save("parents.xlsx")
print("created")