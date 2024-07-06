# Genshindle Solver

Welcome to Genshindle Solver, a tool that helps you solve Genshindle

## Overview

Genshindle Solver is a Python-based application designed to provide a streamlined interface for managing character data in Genshin Impact. It allows users to filter and display character information based on various attributes such as region, element, weapon type, and version.

## Features

- **Data Management:** Load and filter character data stored in Excel format.
- **Version Control:** Automatically checks for updates and downloads new data when available.
- **User Interface:** Simple command-line interface (CLI) for easy interaction.

## Installation

To get started with Genshindle Solver, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/PegaBlade2/genshindle-solver.git
	```

2. Install the required python packages:
	```bash
	pip install -r requirements.txt
	```

3. Run the application:
	```bash
	python solver.py
	```
	
## Usage
There are only 2 commands in this application

### Filter command
This command filters out regions, weapon types, elements, and version
```
filter [type] [value]
There are 4 types, region, weapon, element, and version

Example:
filter region mondstadt
filter weapon !polearm (The ! in this case means not)
filter version <3.0
filter version 1.0
```

### Reset command
This command resets the currently filtered

```
new
```

###### This application was made by PegaBlade
