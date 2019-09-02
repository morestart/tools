# 目录生成树工具

## 使用说明

在根目录运行(python tree.py)即可生成目录树
默认忽略文件及文件夹为
```
ignore_dir = [
    ".pio",
    ".git",
    ".vscode",
    ".idea"
]

ignore_file = [
    "gitattributes",
    "gitignore",
    "yml",
    "travis",
]
```
如果你有其他想要忽略的文件和文件夹,请到修改`ignore_dir`与`ignore_file`两个列表中的数据