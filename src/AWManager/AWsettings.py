import subprocess
import os
import subprocess

def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        return True
    else:
        return False
    

def is_aw_processes_alive():
    processes = ['aw-server', 'aw-watcher-window', 'aw-watcher-afk']
    for process in processes:
        exists = process_exists(process)
        if not exists:
            print(f'[AWsettings] [Error]: {process} does not exist')
            return False
    return True

def find_aw_processes():
    appdata = os.getenv('LOCALAPPDATA')
    dirs = os.listdir(f'{appdata}')
    
    for dir in dirs:
        if 'activitywatch' in dir:
            logs_dir = f'{appdata}\\{dir}'
            
        if 'Programs' in dir:
            programs_dir = f'{appdata}\\{dir}'
            
    programs = os.listdir(programs_dir)
    
    for program in programs:
        if 'ActivityWatch' in program:
            aw_dir = f'{programs_dir}\\{program}'
            
            
    return logs_dir, aw_dir
    
def start_aw_processes(aw_dir):
    subprocess.Popen(['powershell', f'Start-process -FilePath "{aw_dir}\\aw-qt.exe" -WindowStyle Minimized -PassThru'])
    return True

def check_aw_processes():
    is_alive = is_aw_processes_alive()
    
    if not is_alive:
        print('[AWsettings] [Info]: ActivityWatch processes are not running, starting them now...')
        logs_dir, aw_dir = find_aw_processes()
        start_aw_processes(aw_dir)
        return False

