# Count-name Documentation

Welcome to the **Count-name** project documentation! This tool helps you count name frequencies and extract unique names from a text file.

## 🚀 Quick Start

### 1. Prepare Input File
Create a file named `name_to_count.txt` in the same directory as the script. Put the names you want to count in this file, one per line.

### 2. Run the Script
Execute the Python script:
```bash
python "count name.py"
```

### 3. Check Results
- **Console Output**: The script will print the total count of names, list any repeated names with their frequencies, and show the unique name count.
- **Output File**: A file named `name_to_u.txt` will be created (or updated) containing the sorted unique names.
- **Auto-open**: The script will automatically attempt to open the `name_to_u.txt` file for you.

## 🛠️ Features
- **Case Sensitivity**: Currently, the script maintains the original case of the names.
- **Filtering**: Automatically filters out empty lines and single double-quote (`"`) characters.
- **Sorting**: Unique names in the output file are sorted alphabetically.

## 📋 Example
**Input (`name_to_count.txt`):**
```text
Alice
Bob
Alice
Charlie
```

**Output (`name_to_u.txt`):**
```text
Alice
Bob
Charlie
```

**Console Output:**
```text
总共有 4 个名字。
重复的名字:
Alice: 2 次
唯一名字的数量: 3
```

## 📝 License
This project is open-source. Feel free to use and modify!
