import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def count_names_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            raw_data = [line.strip() for line in file]
            # print("原始数据:", raw_data)

            input_data = [
                line for line in raw_data 
                if line and line != '"'
            ]

            # print("过滤后的数据:", input_data)

        total_names = len(input_data)
        name_count = {}
        
        for name in input_data:
            # 保持名字的原始大小写
            name_count[name] = name_count.get(name, 0) + 1

        # 获取重复的名字
        repeated_names = {name: count for name, count in name_count.items() if count > 1}
        unique_names_count = len(name_count)

        return {
            'total_names': total_names,
            'repeated_names': repeated_names,
            'unique_names_count': unique_names_count,
            'name_count': name_count, # 返回完整的名字计数字典
            'sorted_unique_names': sorted(name_count.keys())
        }

    except FileNotFoundError:
        return f"文件 '{filename}' 未找到。"
    except Exception as e:
        return f"发生错误: {e}"

class NameCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Name Counter Tool")
        self.root.geometry("600x500")

        # Input File Selection
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10, fill=tk.X, padx=10)
        
        self.lbl_input = tk.Label(self.input_frame, text="Input File:")
        self.lbl_input.pack(side=tk.LEFT)
        
        self.entry_input = tk.Entry(self.input_frame, width=50)
        self.entry_input.pack(side=tk.LEFT, padx=5)
        self.entry_input.insert(0, "name_to_count.txt")
        
        self.btn_browse = tk.Button(self.input_frame, text="Browse", command=self.browse_file)
        self.btn_browse.pack(side=tk.LEFT)

        # Buttons
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=5)
        
        self.btn_process = tk.Button(self.btn_frame, text="Process & Count", command=self.process_file, bg="#4CAF50", fg="white")
        self.btn_process.pack(side=tk.LEFT, padx=10)

        self.btn_open_input = tk.Button(self.btn_frame, text="Edit Input File", command=self.open_input_file)
        self.btn_open_input.pack(side=tk.LEFT, padx=10)

        # Output Area
        self.txt_output = scrolledtext.ScrolledText(root, width=70, height=20)
        self.txt_output.pack(pady=10, padx=10)

    def browse_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            self.entry_input.delete(0, tk.END)
            self.entry_input.insert(0, filename)

    def open_input_file(self):
        input_file = self.entry_input.get()
        if not os.path.exists(input_file):
            try:
                with open(input_file, 'w', encoding='utf-8') as f:
                    pass
            except Exception as e:
                messagebox.showerror("Error", f"Could not create file: {e}")
                return
        os.startfile(input_file)

    def process_file(self):
        input_file = self.entry_input.get()
        result = count_names_from_file(input_file)

        self.txt_output.delete(1.0, tk.END)
        
        if isinstance(result, str):
            self.txt_output.insert(tk.END, result)
            return

        report = []
        report.append(f"Total Names: {result['total_names']}")
        report.append(f"Unique Names Count: {result['unique_names_count']}\n")
        
        if result['repeated_names']:
            report.append("Repeated Names:")
            for name, count in result['repeated_names'].items():
                report.append(f"  - {name}: {count} times")
        else:
            report.append("No repeated names found.")

        report.append("\n" + "="*30 + "\n")
        
        # Save unique names to file
        output_file_path = 'name_to_output.txt'
        try:
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for unique_name in result['sorted_unique_names']:
                    output_file.write(unique_name + '\n')
            report.append(f"Unique names saved to: {output_file_path}")
            
            # Automatically open the output file (optional, maybe just show in UI)
            # os.startfile(output_file_path) 
            report.append("(Check the output file for the clean list)")
            
        except Exception as e:
            report.append(f"Error saving output file: {e}")

        self.txt_output.insert(tk.END, "\n".join(report))

if __name__ == "__main__":
    root = tk.Tk()
    app = NameCounterApp(root)
    root.mainloop()