"""
1.模块的发布
    a.为什么要发布
        自定义模块切换项目后，不好用
        系统模块切换到新的项目中好用

    b.sys.path
        导入模块时 搜索路径列表
        如果所有的路径都没有要导入的模块，会导致无法导入目标模块
     解决方案 :
        1. 将模块所在的路径手动加入到.path中
        2.  将自定义模块，发布到系统目录
            发布自定义模块的步骤：
                1.确定发布的模块（目录结构）
                    |--setup.py
                    |--package1
                        |
                        --自定义模块 MyMath
                2. setup 的编辑工作
                    setup()
                3. 构建模块
                    python setup.py  build
                4. 发布模块
                    python setup.py sdist



2.模块的安装
    2.1 通过命令完成安装 （推荐）
        a. 找到之前发布的安装包   解压操作
        b. 通过命令安装 发布的压缩包
            python  setup.py install
    2.2 暴力安装
        直接将要安装的包 以及模块  复制到对应的 系统目录中
"""
import sys
list1 = sys.path
print(type(list1))
for path in list1:
    print(path)


