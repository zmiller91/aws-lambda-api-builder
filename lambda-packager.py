import os
import glob
import shutil
from subprocess import call

# make the build directories
base_dir = os.getcwd()
project_name = os.path.basename(base_dir)
build_dir = os.path.join(base_dir, "build")
private_dir = os.path.join(build_dir, "private")
deps_dir = os.path.join(private_dir, "deps")
zip_dir = os.path.join(private_dir, "lib")
output_file = os.path.join(build_dir, project_name)

os.makedirs(deps_dir, exist_ok=True)
os.makedirs(zip_dir, exist_ok=True)

# flatten and copy all python source files to the zip directory
python_files = glob.iglob(os.path.join(base_dir, "**", "*.py"), recursive=True)
for file in python_files:
    if not file.startswith(build_dir) and os.path.isfile(file):
        shutil.copy2(file, zip_dir)

# copy pipfiles to deps directory
shutil.copy2("Pipfile", deps_dir)
shutil.copy2("Pipfile.lock", deps_dir)

# install dependencies in deps directory
os.chdir(deps_dir)
os.environ["PIPENV_VENV_IN_PROJECT"] = deps_dir
call("pipenv install", shell=True)
os.chdir(base_dir)

# move all dependencies to zip directory
python_files = glob.iglob(os.path.join(deps_dir, ".venv", "Lib", "site-packages", "*"))
for file in python_files:
    target_dir_name = os.path.join(zip_dir, os.path.basename(file))
    if not os.path.isdir(file):
        continue

    if os.path.exists(target_dir_name):
        shutil.rmtree(target_dir_name)

    shutil.copytree(file, target_dir_name)

# zip the zip directory
shutil.make_archive(output_file, 'zip', zip_dir)