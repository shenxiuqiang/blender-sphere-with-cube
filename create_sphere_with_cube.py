import bpy

# 清除场景中的所有对象
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# 创建一个球体
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
sphere = bpy.context.active_object
sphere.name = "Sphere"

# 创建一个正方体
bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 1.5))
cube = bpy.context.active_object
cube.name = "Cube"

# 将相机移动到更好的位置以查看场景
if 'Camera' in bpy.data.objects:
    camera = bpy.data.objects['Camera']
    camera.location = (5, 5, 5)
    camera.rotation_euler = (0.9, 0, 2.3)

# 添加光源
bpy.ops.object.light_add(type='SUN', location=(5, 5, 5))

print("已创建球体和正方体")