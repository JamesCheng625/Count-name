# Count-name Documentation

Welcome to the **Count-name** project documentation! This tool helps you count name frequencies and extract unique names from a text file, featuring a user-friendly graphical interface (GUI).

## 📥 Installation

### 1. Install Python
Ensure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

### 2. Install Dependencies
This project uses standard libraries, but if you want to build the executable, you'll need `pyinstaller`.
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Option 1: Run with Python
You can run the script directly if you have Python installed.

1.  Open a terminal/command prompt in the project folder.
2.  Run the following command:
    ```bash
    python count_name.py
    ```
3.  The GUI window will appear.

### Option 2: Run the Executable (.exe)
If you have built or downloaded the `.exe` file, simply double-click it to launch the application. No Python installation is required for this method.

### Using the Interface
1.  **Input File**: The default input file is `name_to_count.txt`. You can click **Browse** to select a different file.
2.  **Edit Input**: Click **Edit Input File** to open the selected text file and add/modify names.
3.  **Process**: Click **Process & Count** to run the analysis.
4.  **Results**:
    - The stats (Total keys, Unique counts, Repetitions) will be shown in the text area.
    - A clean list of unique names will be saved to `name_to_output.txt`.

## 📦 Building the Executable (.exe)
You can convert this Python script into a standalone `.exe` file so it can be run on any Windows computer without installing Python.

1.  Make sure you have installed the requirements:
    ```bash
    pip install pyinstaller
    ```

2.  Run the build command:
    ```bash
    pyinstaller --onefile --windowed --name "NameCounter" count_name.py
    ```
    * `--onefile`: Bundles everything into a single .exe file.
    * `--windowed`: Prevents a black console window from appearing (good for GUI apps).

3.  Find your app:
    - The new `.exe` file will be located in the `dist/` folder.

## 🛠️ Features
- **User-Friendly UI**: Simple graphical interface for easy operation.
- **Name Counting**: Calculates total names and identifies duplicates.
- **Unique List**: Generates a sorted, duplicate-free list (`name_to_output.txt`).
- **Input Filtering**: Ignores empty lines.

## 📋 Example
**Input File Content:**
```text
Alice
Bob
Alice
Charlie
```

**Result:**
- **Total Names**: 4
- **Unique Names**: 3
- **Repeated**: Alice (2 times)
- **Output File**: Contains `Alice`, `Bob`, `Charlie` sorted.

## 📝 License
This project is open-source. Feel free to use and modify!
