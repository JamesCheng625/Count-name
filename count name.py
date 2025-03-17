import os

def count_names_from_file(filename):
    try:
        with open(filename, 'r') as file:
            raw_data = [line.strip() for line in file]
            print("原始数据:", raw_data)

            input_data = [
                line for line in raw_data 
                if line and line != '"'
            ]

            print("过滤后的数据:", input_data)

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
            'name_count': name_count  # 返回完整的名字计数字典
        }

    except FileNotFoundError:
        return f"文件 '{filename}' 未找到。"
    except Exception as e:
        return f"发生错误: {e}"

# 示例用法
result = count_names_from_file(r'C:\Users\jamescheng\Desktop\code\xlsx\name_to_count.txt')
print(f"总共有 {result['total_names']} 个名字。")

if result['repeated_names']:
    print("重复的名字:")
    for name, count in result['repeated_names'].items():
        print(f"{name}: {count} 次")

# 写入唯一名字到文件，每次运行时替换文件内容
output_file_path = r'C:\Users\jamescheng\Desktop\code\xlsx\name_to_u.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for unique_name in result['name_count'].keys():  # 获取唯一名字
        output_file.write(unique_name + '\n')  # 每个名字后加换行符

print(f"唯一名字的数量: {result['unique_names_count']}")  # 打印唯一名字的数量

# 自动打开输出文件
os.startfile(output_file_path)
