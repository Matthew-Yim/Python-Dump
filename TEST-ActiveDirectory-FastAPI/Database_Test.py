import sqlite3
import subprocess

Get_ADUSERS = "Get-ADUser -Filter * -Properties SID, Name, Title, Department, Office, UserPrincipalName, ThumbnailPhoto | Select-Object -First 20 SID, Name, Title, Department, Office, UserPrincipalName, ThumbnailPhoto"

def run_powershell(powershell_script):
    # Execute the PowerShell command
    result = (subprocess.run(f'powershell.exe -Command "{powershell_script}"', capture_output=True, text=True))
    output = result.stdout
    # Process the output line by line
    lines = []
    for line in result.stdout.splitlines():
        # Skip empty lines
        lines = output.split('\n')
        data_rows = []
        for line in lines[1:-1]:  # Skip header and footer lines
            fields = line.split(',')
            print(fields[0])
            if fields:
                data_rows.append(fields)
    return data_rows

data_rows = run_powershell(Get_ADUSERS)
conn = sqlite3.connect('AppData.db')

cursor = conn.cursor()

records = []
for row in data_rows:
    print(row.t)
    # cursor.executemany("INSERT INTO AdUsers (SID, Name, Title, Department, Office, UserPrincipalName, ThumbnailPhoto) VALUES (?, ?, ?, ?, ?, ?, "")", row)
cursor.commit()
cursor.close()