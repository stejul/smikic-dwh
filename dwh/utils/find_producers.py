import os
import sys

from pathlib import Path
from importlib import import_module

def find_stream():
    result = []
    file_prefix = "_stream.py" 
    """
    for root, dir, files in os.walk("./dwh"):
        for file in files:
            if file.endswith(file_prefix):
                #plugin_module = import_module(file)
                #print(plugin_module)
                print(dir)
                result.append(file)
    print(result)
    """
    for subdir, dirs, files in os.walk("."):
        for file in files:
            if file.endswith("_stream.py"):
                mod = os.path.basename(os.path.dirname(f"{subdir}/{file}"))
                result.append(f"{mod}.{file[:-3]}")
                print(f"{mod}/{file}")
                #sys.path.append(f"{mod}/{file}")
                
                #plugin_module = import_module(f"{mod}.{file[:-3]}", ".")
                
                
                #print(plugin_module)
    print(result)

    for plugin in result:
        print(plugin)
        
        modul = import_module(plugin, ".")

if __name__ == "__main__":
    find_stream()
	
