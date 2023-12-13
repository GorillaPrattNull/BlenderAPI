import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *

#~ <bpy_collection[2], BlendDataMaterials>
#~ 
list(bpy.data.objects)
#~ [bpy.data.objects['Camera'], bpy.data.objects['Cube'], bpy.data.objects['Light']]
#~ 
bpy.data.object['Cube']
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#! AttributeError: 'BlendData' object has no attribute 'object'
#! 
bpy.data.object["Cube"]
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#! AttributeError: 'BlendData' object has no attribute 'object'
#! 
bpy.data.objects["Cube"]
#~ bpy.data.objects['Cube']
#~ 
bpy.data.objects[0]
#~ bpy.data.objects['Camera']
#~ 
bpy.data.objects[0].name
#~ 'Camera'
#~ 
bpy.data.scenes["Scene"]
#~ bpy.data.scenes['Scene']
#~ 
list(bpy.data.materials)
#~ [bpy.data.materials['Dots Stroke'], bpy.data.materials['Material']]
#~ 
list(bpy.data.materials)
#~ [bpy.data.materials['Dots Stroke'], bpy.data.materials['Material']]
#~ 
bpy.data.materials.new("MyMaterial")
#~ bpy.data.materials['MyMaterial']
#~ 
list(bpy.data.materials)
#~ [bpy.data.materials['Dots Stroke'], bpy.data.materials['Material'], bpy.data.materials['MyMaterial']]
#~ 
bpy.data.scenes[0].render.resolution_percentage
#~ 100
#~ 
bpy.data.scenes[0].render.resolution_
bpy.data.scenes[0].render.resolution_
bpy.data.scenes[0].render.resolution_x
#~ 1920
#~ 
bpy.data.scenes[0].render.resolution_y
#~ 1080
#~ 
bpy.data.scenes[0].objects["Torus"].data.vertices[0].co.x
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#! KeyError: 'bpy_prop_collection[key]: key "Torus" not found'
#! 
bpy.data.scenes[0].objects["Cube"].data.vertices[0].co.x
#~ 1.0
#~ 
mesh = bpy.data.meshes.new(name="MyMesh")
print(mesh)
#~ <bpy_struct, Mesh("MyMesh") at 0x0000020ED6979608>
#~ 
bpy.context.object["MyOwnProperty"] = 42

if "SomeProp" in bpy.context.object:
    print("Property found")

# Use the get function like a Python dictionary
# which can have a fallback value.
value = bpy.data.scenes["Scene"].get("test_prop", "fallback value")

# dictionaries can be assigned as long as they only use basic types.
collection = bpy.data.collections.new("MyTestCollection")
collection["MySettings"] = {"foo": 10, "bar": "spam", "baz": {}}

bpy.data.objects[0].name
#~ 'Camera'
#~ 





bpy.context.object["MyOwnProperty"] = 42
if "SomeProp" in bpy.context.object:
    print("Property found")
    if "SomeProp" in bpy.context.object:
    print("Property found")
#!   File "<blender_console>", line 4
#!     print("Property found")
#!     ^^^^^
#! IndentationError: expected an indented block after 'if' statement on line 3
#! 
value = bpy.data.scenes["Scene"].get("test_prop", "fallback value")
collection = bpy.data.collections.new("MyTestCollection")
collection["MySettings"] = {"foo": 10, "bar": "spam", "baz": {}}
del collection["MySettings"]
bpy.context.object["MyOwnProperty"] = 42

if "SomeProp" in bpy.context.object:
    print("Property found")
    


bpy.context.object["MyOwnProperty"] = 42
    if "SomeProp" in bpy.context.object: print("Property found")
#!   File "<blender_console>", line 1
#!     if "SomeProp" in bpy.context.object: print("Property found")
#! IndentationError: unexpected indent
#! 
    if "SomeProp" in bpy.context.object: print("Property found")
#!   File "<blender_console>", line 1
#!     if "SomeProp" in bpy.context.object: print("Property found")
#! IndentationError: unexpected indent
#! 
    if "SomeProp" in bpy.context.object: print("Property found")
#!   File "<blender_console>", line 1
#!     if "SomeProp" in bpy.context.object: print("Property found")
#! IndentationError: unexpected indent
#! 
if "SomeProp" in bpy.context.object:
    print("Property found")
    
 bpy.context.object["MyOwnProperty"] = 42
#!   File "<blender_console>", line 1
#!     bpy.context.object["MyOwnProperty"] = 42
#! IndentationError: unexpected indent
#! 
bpy.context.object["MyOwnProperty"] = 42
if "SomeProp" in bpy.context.object:
    print("Property found")
    
if "MyOwnProperty" in bpy.context.object:
    print("Property found")
    
#~ Property found
#~ 
value = bpy.data.scenes["Scene"].get("test_prop", "fallback value")
value
#~ 'fallback value'
#~ 
list(bpy>context)
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#! NameError: name 'context' is not defined
#! 
list(bpy.context)
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#! TypeError: 'Context' object is not iterable
#! 
list(bpy.context.object)
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#! TypeError: 'Object' object is not iterable
#! 
bpy.context
#~ <bpy_struct, Context at 0x0000020ECDD3D088>
#~ 
bpy.context.object
#~ bpy.data.objects['Cube']
#~ 
bpy.context.object
#~ bpy.data.objects['Camera']
#~ 
bpy.context.view_layer.objects.active = obj
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#! NameError: name 'obj' is not defined
#! 
bpy.context.view_layer.objects.active = Cube
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#! NameError: name 'Cube' is not defined
#! 
bpy.context.view_layer.objects.active
#~ bpy.data.objects['Camera']
#~ 
bpy.context.view_layer.objects.active = "Cube"
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#! TypeError: BPy_PropertyRNA - Attribute (setattr): LayerObjects.active expected a Object type, not str
#! 
bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
bpy.context.view_layer.objects.active = bpy.data.objects['Camera']
bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
bpy.context.view_layer.objects.active = bpy.data.objects['Light']
bpy.ops.mesh.hide(unselected=False)
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#!   File "D:\Apps\Blender\3.6\3.6\scripts\modules\bpy\ops.py", line 113, in __call__
#!     ret = _op_call(self.idname_py(), None, kw)
#! RuntimeError: Operator bpy.ops.mesh.hide.poll() failed, context is incorrect
#! 
bpy.ops.mesh.hide(unselected=False)
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#!   File "D:\Apps\Blender\3.6\3.6\scripts\modules\bpy\ops.py", line 113, in __call__
#!     ret = _op_call(self.idname_py(), None, kw)
#! RuntimeError: Operator bpy.ops.mesh.hide.poll() failed, context is incorrect
#! 
bpy.ops.mesh.hide
#~ bpy.ops.mesh.hide(unselected=False)
#~ 
bpy.ops.mesh.hide(unselected=True)
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#!   File "D:\Apps\Blender\3.6\3.6\scripts\modules\bpy\ops.py", line 113, in __call__
#!     ret = _op_call(self.idname_py(), None, kw)
#! RuntimeError: Operator bpy.ops.mesh.hide.poll() failed, context is incorrect
#! 
bpy.ops.mesh.flip_normals()
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#!   File "D:\Apps\Blender\3.6\3.6\scripts\modules\bpy\ops.py", line 113, in __call__
#!     ret = _op_call(self.idname_py(), None, kw)
#! RuntimeError: Operator bpy.ops.mesh.flip_normals.poll() failed, context is incorrect
#! 
bpy.ops.object.transform_apply()
#~ {'FINISHED'}
#~ 
bpy.ops.view3d.render_border()
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#!   File "D:\Apps\Blender\3.6\3.6\scripts\modules\bpy\ops.py", line 113, in __call__
#!     ret = _op_call(self.idname_py(), None, kw)
#! RuntimeError: Operator bpy.ops.view3d.render_border.poll() failed, context is incorrect
#! 
if bpy.ops.view3d.render_border.poll():
    bpy.ops.view3d.render_border()
    

if bpy.ops.view3d.render_border.poll():
    bpy.ops.view3d.render_border()
    

if bpy.ops.view3d.render_border.poll():
    bpy.ops.view3d.render_border()
    

bpy.ops.view3d.render_border()
#! Traceback (most recent call last):
#!   File "<blender_console>", line 1, in <module>
#!   File "D:\Apps\Blender\3.6\3.6\scripts\modules\bpy\ops.py", line 113, in __call__
#!     ret = _op_call(self.idname_py(), None, kw)
#! RuntimeError: Operator bpy.ops.view3d.render_border.poll() failed, context is incorrect
#! 
if bpy.ops.view3d.render_border.poll():
    bpy.ops.view3d.render_border()
    
