#!/usr/bin/env python
import subprocess
from pathlib import Path
import os


def poetry_install() -> str:
    print("Running poetry install")
    
    poetry_install_command = subprocess.run(["poetry", "install"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if poetry_install_command.returncode == 0:
        poetry_env_info_command = subprocess.run(["poetry", "env", "info", "--path"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        return poetry_env_info_command.stdout.replace(os.linesep, "")
    return None
    
def replace_poetry_env_vscode_settings(poetry_venv_path: str) -> None:
    vscode_settings_original_file_path = Path(".vscode/settings.json")
    vscode_settings_rendered_file_path = Path(".vscode/settings.json.tmp")
    
    print(f"Updating the file {vscode_settings_original_file_path.absolute()} with the right Poetry virtualenv path")
    
    with vscode_settings_original_file_path.open(mode = "r") as vscode_settings_original, vscode_settings_rendered_file_path.open(mode = "a+") as vscode_settings_rendered:
        for line in vscode_settings_original:
            vscode_settings_rendered.write(line.replace("%%POETRY_VENV_PATH%%", poetry_venv_path))
            
    vscode_settings_original_file_path.unlink()
    vscode_settings_rendered_file_path.rename(".vscode/settings.json")


if __name__ == "__main__":
    poetry_venv_path = poetry_install()
    replace_poetry_env_vscode_settings(poetry_venv_path)
