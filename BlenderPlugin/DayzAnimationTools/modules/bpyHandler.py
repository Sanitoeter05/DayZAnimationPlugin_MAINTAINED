import bpy
def registerClasses(classes):
    for cls in classes:
        bpy.utils.register_class(cls)

def registerMenus(menus, menuClass):
    for menu in menus:
        getattr(bpy.types, menuClass).append(menu)

def unregisterClasses(classes):
    for cls in classes:
        bpy.utils.unregister_class(cls)

def unregisterMenus(menus, menuClass):
    for menu in menus:
        getattr(bpy.types, menuClass).remove(menu)

def getOperator(context):
    sfile = context.space_data
    operator = sfile.active_operator
    return operator