import os

from pathlib import Path
from importlib import import_module

def find_producers():
    result = []
    file_prefix = "listener.py" 
    for subdir, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(file_prefix):
                mod = os.path.basename(os.path.dirname(f"{subdir}/{file}"))
                # create string that corresponds to correct package string for importing
                # [:-3] removes ".py" from file string
                result.append(f"dwh.{mod}.{file[:-3]}")
    print(result)

    for plugin in result:
        print(plugin)
        module_lib = import_module(plugin, ".")
        print(module_lib.TwitterListener().TOPIC_NAME)

if __name__ == "__main__":
    find_producers()
	
