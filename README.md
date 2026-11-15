# Git Patch Demo

这是一个用于学习 Git 分支和 patch 的最小示例项目。

运行程序：

```bash
python3 app.py
python3 app.py --name 小明
```

查看分支：

```bash
git branch -v
```

## 自动化测试

在本地运行单元测试：

```bash
python3 -m unittest -v
```

向 `master` 提交 Pull Request 时，GitHub Actions 会自动运行测试。测试通过后才能合并。
