Figure this out. How does one find an object on the scene and run functions on it and change internal values related to it

bpy.context.object
bpy.data.objects['Cube']
C.scene.objects
bpy.data.scenes['Scene'].objects
Note that these types reference Blender’s data so modifying them is visible immediately.

Mathutils Types
Accessible from mathutils are vectors, quaternions, Euler angles, matrix and color types. Some attributes such as bpy.types.Object.location, bpy.types.PoseBone.rotation_euler and bpy.types.Scene.cursor_location can be accessed as special math types which can be used together and manipulated in various useful ways.

Example of a matrix, vector multiplication:

bpy.context.object.matrix_world @ bpy.context.object.data.verts[0].co
Note

mathutils types keep a reference to Blender’s internal data so changes can be applied back.

Example:

# modifies the Z axis in place.
bpy.context.object.location.z += 2.0

# location variable holds a reference to the object too.
location = bpy.context.object.location
location *= 2.0

# Copying the value drops the reference so the value can be passed to
# functions and modified without unwanted side effects.
location = bpy.context.object.location.copy()
