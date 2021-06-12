from platform import system
import os
from PyInquirer import prompt
# The OS
#    Linux: Linux
#    Mac: Darwin
#    Windows: Windows

OS = system()
print("You are running:", OS)

linux_questions = [
    {
        'type': 'list',
        'name': 'shell',
        'message': 'What shell do you use?',
        'choices': ['bash', 'zsh']
    },
    {
        'type': 'input',
        'name': 'ip',
        'message': 'What is the IP of the mirror? (including "http://")',
    }
]

windows_questions = [
    {
        'type': 'input',
        'name': 'ip',
        'message': 'What is the IP of the mirror? (including "http://")',
    }
]

rc_files = {
    'bash' : '~/.bashrc',
    'zsh' : '~/.zshrc'
}

# Linux script for install command
linux_script = """
echo "Writting to {rcfile}"
echo "alias mirror-install=pip install --trusted-host {ip} -i {ip}" >> {rcfile}
echo "Restart your shell, and run mirror-install instead of pip-install"
"""

# Windows script for installing
windows_script = """
@echo off

:: Temporary system path at cmd startup

DOSKEY mirror-install=pip install --trusted-host {ip} -i {ip}"
"""

# The windows regestry editor file
regedit = """Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Command Processor]
"AutoRun"="%USERPROFILE%\\pipmirror.cmd"""

if OS == "Linux" or OS == "Darwin":
    answers = prompt(linux_questions)
    # script is generated
    script = linux_script.format(ip = answers['ip'], rcfile = rc_files[answers['shell']])

    with open('script.sh', 'w') as f:
        # Write file
        f.write(script)

    # Info file
    print("Script has been written as 'script.sh'")
    print("Attempting to chmod the script to executable...")
    os.system("chmod +x script.sh")
    print("In order to use the mirror conviently, run script.sh\nThen restart your shell, and run mirror-install instead of pip-install")

elif OS == "Windows":
    answers = prompt(linux_questions)
    # script is generated
    script = windows_script.format(ip = answers['ip'])

    with open("%USERPROFILE%\\pipmirror.cmd", 'w') as f:
        # Write file
        f.write(script)
    

    with open("mirror.reg", 'w') as f:
        # Regedit file writer
        f.write(regedit)
    
    print("In order to use the mirror-install command, you have to the mirror.reg regedit file. This will add %USERPROFILE%\\pipmirror.cmd, which writes an alias, to autostart.")