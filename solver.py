import pandas as pd
import os
import requests
import shutil

# Constants
VERSION_FILE = "current_version.txt"
VERSION_URL = "https://raw.githubusercontent.com/PegaBlade2/genshindle-solver/main/updates/version.txt"  # URL that returns the latest version
DOWNLOAD_URL = "https://raw.githubusercontent.com/PegaBlade2/genshindle-solver/main/updates/characters_database.xlsx"  # Direct download URL to download the new file
FILE_PATH = "characters_database.xlsx"  # Path to the file that needs to be replaced

def get_current_version():
    try:
        with open(VERSION_FILE, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Version file {VERSION_FILE} not found. Assuming version is 0.0")
        return "0.0"

def check_version():
    try:
        response = requests.get(VERSION_URL)
        response.raise_for_status()
        latest_version = response.text.strip()
        return latest_version
    except requests.RequestException as e:
        print(f"Error checking for latest version: {e}")
        return None

def download_new_file():
    try:
        with requests.get(DOWNLOAD_URL, stream=True) as r:
            r.raise_for_status()
            with open(FILE_PATH, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print("File downloaded and replaced successfully.")
    except requests.RequestException as e:
        print(f"Error downloading the new file: {e}")

def update_version_file(new_version):
    try:
        with open(VERSION_FILE, 'w') as file:
            file.write(new_version)
    except IOError as e:
        print(f"Error updating version file: {e}")

def main():
    current_version = get_current_version()
    latest_version = check_version()
    if latest_version:
        if latest_version != current_version:
            print(f"New version available: {latest_version}. Downloading update...")
            download_new_file()
            update_version_file(latest_version)
        else:
            print("You are using the latest version.")
    else:
        print("Could not check for updates. Proceeding with the current version.")

    # Load the Excel file
    df = pd.read_excel(FILE_PATH)
    df_filtered = df.copy()

    # Set display options to show all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    while True:
        # Get the user input
        command = input('> ')

        # Check if the command is "new"
        if command.lower() == 'new':
            df_filtered = df.copy()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("New session started.")
            continue

        # Split the command into parts
        parts = command.split()

        # Check if the command is "filter"
        if parts[0].lower() == 'filter':
            column_name = None
            filter_value = parts[2].lower()

            if parts[1].lower() == 'region':
                column_name = 'Region'
            elif parts[1].lower() == 'element':
                column_name = 'Element'
            elif parts[1].lower() == 'weapon':
                column_name = 'Weapon Type'
            elif parts[1].lower() == 'version':
                column_name = 'Version'

            if column_name is None:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid filter type. Use 'region', 'element', 'weapon', or 'version'.")
                continue

            # Check if the filter value is negated
            if filter_value.startswith('!'):
                filter_value = filter_value[1:]
                if column_name == 'Version':
                    if filter_value.startswith('<'):
                        df_filtered = df_filtered[df_filtered[column_name] < float(filter_value[1:])]
                    elif filter_value.startswith('>'):
                        df_filtered = df_filtered[df_filtered[column_name] > float(filter_value[1:])]
                    else:
                        df_filtered = df_filtered[df_filtered[column_name].astype(str).str.lower() != filter_value]
                else:
                    df_filtered = df_filtered[df_filtered[column_name].astype(str).str.lower() != filter_value]
            else:
                if column_name == 'Version':
                    if filter_value.startswith('<'):
                        df_filtered = df_filtered[df_filtered[column_name] < float(filter_value[1:])]
                    elif filter_value.startswith('>'):
                        df_filtered = df_filtered[df_filtered[column_name] > float(filter_value[1:])]
                    else:
                        df_filtered = df_filtered[df_filtered[column_name] == float(filter_value)]
                else:
                    df_filtered = df_filtered[df_filtered[column_name].astype(str).str.lower() == filter_value]

            # Clear the console
            os.system('cls' if os.name == 'nt' else 'clear')

            # Print the filtered results
            print(df_filtered)

            # Print the count of each filter value
            print("\nFilter Value Counts:")
            for column in ['Region', 'Element', 'Weapon Type', 'Version']:
                print(f"{column}:")
                print(df_filtered[column].value_counts())
                print()

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid command. Type 'filter' to filter the data or 'new' to start a new session.")

if __name__ == "__main__":
    main()
