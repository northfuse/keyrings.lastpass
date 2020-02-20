import shutil
import subprocess

def lastpass_installed():
    return bool(shutil.which("lpass"))

def lpass(*args):
    cli_args = ["lpass"] + list(args)
    result = subprocess.run(args, stdout=subprocess.PIPE, check=True)
    print(result)
    return result
