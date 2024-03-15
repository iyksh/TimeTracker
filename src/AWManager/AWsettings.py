import subprocess
import os
import subprocess

def process_exists(process_name) -> bool:
    """Check if a process is running"""
    
    try:
        progs = str(subprocess.check_output('tasklist'))
        if process_name in progs:
            return True
        else:
            return False
    except Exception as e:
        print(f'[AWsettings] [Error]: {e}')
        print(f'[AWsettings] [Error]: Probably the process "{process_name}" does not exist')
        
        return False
    

def is_aw_processes_alive() -> list:
    """Check if the ActivityWatch processes are running"""
    
    processes = ['aw-server', 'aw-watcher-afk', 'aw-watcher-window', 'aw-qt']
    is_alive = []
    
    for process in processes:
        exists = process_exists(process)
        is_alive.append(exists)
        
    return is_alive

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

    aw_server_path = aw_dir[1] + '\\aw-server\\aw-server.exe'
    aw_watcher_afk_path = aw_dir[1] + '\\aw-watcher-afk\\aw-watcher-afk.exe'
    aw_watcher_window_path = aw_dir[1] + '\\aw-watcher-window\\aw-watcher-window.exe'
    
    subprocess.Popen(['powershell', f'Start-process -FilePath "{aw_server_path}" -WindowStyle Hidden -PassThru'])
    subprocess.Popen(['powershell', f'Start-process -FilePath "{aw_watcher_afk_path}" -WindowStyle Hidden -PassThru'])
    subprocess.Popen(['powershell', f'Start-process -FilePath "{aw_watcher_window_path}" -WindowStyle Hidden -PassThru'])
    
    return True

def check_aw_processes():
    is_alive = is_aw_processes_alive()
    
    for alive in is_alive:
        if not alive and is_alive.index(alive) != 3:
            print(f'[AWsettings] [Info]: ActivityWatch processe {is_alive.index(alive)} are not running, starting them now...')
            aw_dir = find_aw_processes()
            start_aw_processes(aw_dir)
            break
        
    
    kill_qt()
        
    

def kill_qt() -> None:
    """Kill the aw-qt process to the user doesn't see the Dashboard"""
    
    while process_exists('aw-qt'):
        subprocess.Popen(['powershell', f'Stop-Process -Name "aw-qt"'])
    
    
