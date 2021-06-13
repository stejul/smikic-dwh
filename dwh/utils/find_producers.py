import os

from pathlib import Path
from importlib import import_module

def find_producers():
    result = []
    classes = []
    file_path = []
    file_prefix = "listener.py" 
    for subdir, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(file_prefix):
                mod = os.path.basename(os.path.dirname(f"{subdir}/{file}"))
                # create string that corresponds to correct package string for importing
                # [:-3] removes ".py" from file string
                #print(f"{subdir[2:]}/{file}")
                result.append(f"dwh.{mod}.{file[:-3]}")
                file_path.append(f"{subdir[2:]}/")

    #print(result)

    for plugin, filePath in zip(result,file_path):
        #print(plugin, filePath)
        module_lib = import_module(plugin, ".")
        classes.append({"topic_name": getattr(module_lib.Listener(), "TOPIC_NAME"), "file_path": filePath})

    return classes

if __name__ == "__main__":
    find_producers()
	
