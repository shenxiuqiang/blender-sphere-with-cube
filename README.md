# Blender 球体与正方体

这个仓库包含一个简单的Blender Python脚本，用于创建一个球体并在其上方放置一个正方体。

## 功能

脚本执行以下操作：

1. 清除当前场景中的所有对象
2. 创建一个半径为1的球体，位于原点(0, 0, 0)
3. 创建一个边长为0.5的立方体，位于球体上方(0, 0, 1.5)
4. 调整相机位置以便更好地查看场景
5. 添加一个太阳光源以照亮场景

## 使用方法

### 方法1：在Blender内运行

1. 打开Blender
2. 切换到"Scripting"工作区
3. 在文本编辑器中创建一个新文件
4. 将`create_sphere_with_cube.py`中的代码复制粘贴到编辑器中
5. 点击"Run Script"按钮运行脚本

### 方法2：从命令行运行

```bash
blender --background --python create_sphere_with_cube.py
```

### 方法3：从Blender文件浏览器运行

1. 打开Blender
2. 按下`Shift + F1`打开文件浏览器
3. 导航到`create_sphere_with_cube.py`文件所在位置
4. 选中该文件并点击"Open"
5. 点击"Run Script"按钮运行脚本

## 效果预览

运行脚本后，您将看到一个位于原点的球体，球体上方有一个正方体。场景已经设置好灯光和相机角度，可以直接渲染查看效果。

## 自定义

您可以通过修改脚本中的参数来自定义对象：

- 球体半径：修改`primitive_uv_sphere_add`函数中的`radius`参数
- 球体位置：修改`primitive_uv_sphere_add`函数中的`location`参数
- 立方体大小：修改`primitive_cube_add`函数中的`size`参数
- 立方体位置：修改`primitive_cube_add`函数中的`location`参数