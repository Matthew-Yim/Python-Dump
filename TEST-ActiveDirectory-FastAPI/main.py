import json
import sqlite3

import uvicorn
from fastapi import FastAPI

app = FastAPI()

# Packages
import subprocess

# Powershell Scripts
Get_NewUsers = \
    """
    function Get-NewUsers{
        $date = (Get-Date).AddDays(-30).Date
        get-aduser -filter {whencreated -ge $date} -properties title,created | select name,created,title | Sort-Object {$_.created -as [DateTime]} -Descending
    }
    
    Get-NewUsers | ConvertFrom-Csv
    """

Get_ADUSERS = "Get-ADUser -Filter * -Properties SID, Name, Title, Department, Office, UserPrincipalName, ThumbnailPhoto | Select-Object -First 20 SID, Name, Title, Department, Office, UserPrincipalName, ThumbnailPhoto"

# Helper Functions
def run_powershell(powershell_script):
    # Execute the PowerShell command
    result = (subprocess.run(f'powershell.exe -Command "{powershell_script}"', capture_output=True, text=True))

    # Process the output line by line
    lines = []
    for line in result.stdout.splitlines():
        # Skip empty lines
        if not line.strip():
            continue

        # Remove the '@{' prefix and the '}' suffix
        obj_str = line.replace('@{', '').replace('}', '')

        # Split the remaining string by '; '
        key_value_pairs = obj_str.split('; ')
        if (len(key_value_pairs) != 1):
            lines.append(key_value_pairs)
    return lines


def parse_powershell_output(lines):
    users_data = []

    for line in lines:
        # N number of element representing N number of fields/columns
        user_dict = {}
        for pair in line:
            key, value = pair.split('=')
            if key.strip() == 'name':
                user_dict['name'] = value.strip()
            elif key.strip() == 'created':
                user_dict['created'] = value.strip()
            elif key.strip() == 'title':
                user_dict['title'] = value.strip()
        users_data.append(user_dict)

    return users_data


# Endpoints
@app.get("/")
async def root():
    command = 'powershell.exe -Command "whoami"'
    result = (subprocess.run(command, capture_output=True, text=True)) \
        .stdout.strip().split('\\')[-1] \
        .title().replace('.', ' ')
    return {"messagez": f"Goodbye: {result}"}


@app.get("/new-users")
async def get_new_users():
    lines = run_powershell(Get_NewUsers)
    result = parse_powershell_output(lines)
    return json.loads(json.dumps(result, indent=2))

@app.get("/ad-users")
async def get_ad_users():
    lines = run_powershell(get_ad_users)
    result = parse_powershell_output(lines)
    return json.loads(json.dumps(result, indent=2))


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/try-dbconnection")
async def try_dbConnection():
    try:
        sqliteConnection = sqlite3.connect('AppData.db')
        cursor = sqliteConnection.cursor()
        print("Database Initialized")

        query = "SELECT * From AdUsers"
        cursor.execute(query)

        result = cursor.fetchall()
        for item in result:
            print("kiwi")
            print(item)
        cursor.close()
        return{"kiwi": "yes"}
    except sqlite3.Error as error:
        print('Error occurred - ', error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed')

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)  # Running on port 8001