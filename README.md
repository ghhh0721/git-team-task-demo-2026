# 待办清单命令行程序

一个用于练习 Git 分支、Pull Request 和代码审查的小项目，只依赖 Python 标准库。

## 运行

需要 Python 3.9 或更高版本。在本目录运行：

```powershell
python tasks.py add "完成 Git 作业"
python tasks.py list
python tasks.py done 1
```

任务保存在当前目录的 `tasks.json` 中；该文件不会提交到仓库。
