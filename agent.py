from pathlib import Path
from rules import rules
from log import log_action

def check_exists():
    path = Path("/Users/wesleydeal/Desktop")
    for folder in rules.keys():
        if not (path / folder).exists():
            print(f"Missing folder: {folder}")
            (path / folder).mkdir()
            print(f"Folder created: {folder}")

# create path where agent will run; in this case, it will clean the desktop
def clean():
    path = Path("/Users/wesleydeal/Desktop")

    folders = [] # list to hold folder names that are found and not moved

    for file in path.iterdir():
        if file.is_dir():
            folders.append(file.name)
        else:
            for key, values in rules.items():
                if file.suffix in values:
                    print(f"File {file} will be moved to {key} folder.")
                    log_action(action="move", file_name=file, folder_name=key)
                    break
                else:
                    print(f"File {file} does not match any rule and will move to Other Files folder.")
                    break

    return folders


if __name__ == "__main__":
    check_exists()
    folders = clean()
    print("Folders found and unmoved: ")
    for folder in folders:
        print(folder)
          