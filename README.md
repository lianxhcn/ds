# Data Analysis Course

## 下载本仓库-课件

- 点击绿色 **<font color=green><>Code</font>** 按钮，选择 **Download ZIP** 下载本仓库。
- 解压缩后，使用 VS Code 打开文件夹即可。
- 上课演示的 `.ipynb` 文件在 **./body** 文件夹中，文件名与 [DSbook](https://book.lianxh.cn/ds/index.html) 的网址中的文件名对应。
  - <https://lianxhcn.github.io/ds/body/01_02_jupyter_notebook.html>
  - 对应 `./body/01_02_jupyter_notebook.ipynb` 文件

## 使用 github desktop 下载

如果你熟悉 git，可以在 VScode 终端使用 git 命令 Fork 或 clone 本仓库。对于多数人来说，推荐使用 [GitHub Desktop](https://desktop.github.com/)，详情参见：

  - 杨雪, 2025, [GitHub Desktop 使用方法介绍：可视化 Git 管理的效率工具](https://www.lianxh.cn/details/1672.html).

实操过程中遇到问题，可以问一下 DeepSeek 或豆包。

## 发布自己的在线讲义

你可以修改本仓库的内容，发布自己的在线讲义。具体步骤如下：

- 在 GitHub 上 Fork 本仓库。
- 在本地使用 GitHub Desktop 或 git 命令将 Fork 后的仓库 clone 到本地。
- 修改内容后，在 VScode 终端执行 `quarto render` 命令生成新的网页内容。在此之前，你需要安装 [Quarto](https://quarto.org/docs/get-started/)，以及 VScode 的 [Quarto 扩展](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)。
- 使用 GitHub Desktop 或 git 命令将修改后的内容 push 到 GitHub 上。
- 在 GitHub 上打开你的仓库，点击 **Settings**，选择 **Pages**，在 **Source** 处选择 **main branch**，然后点击 **Save**。
- 稍等几分钟后，你的在线讲义就会发布成功，网址为 `https://你的用户名.github.io/ds/`。

详情参见：连玉君，2025，[Quarto Book](https://lianxhcn.github.io/quarto_book/)。