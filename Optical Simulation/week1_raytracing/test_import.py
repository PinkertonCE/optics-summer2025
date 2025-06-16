import os
print("Files in this folder:")
print(os.listdir())

try:
    import optics
    print("optics successfully imported:")
    print(dir(optics))
except Exception as e:
    print("failed to import optics:", e)
    
try:
    import visualization
    print("optics successfully imported:")
    print(dir(visualization))
except Exception as e:
    print("failed to import visualization:", e)