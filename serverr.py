import subprocess
import time
import psutil

# Join :- @JAVAxCheaT # Define the command to send to the terminal
command = "echo 'Script stopped, restarting...' && python loop.py"

# Join :- @JAVAxCheaT # Define the script to monitor
script_to_monitor = "loop.py"

# Join :- @JAVAxCheaT # Get the process ID of the script to monitor
script_pid = None
for proc in psutil.process_iter():
    try:
        if proc.name() == 'python' and any(script_to_monitor in part for part in proc.cmdline()):
            script_pid = proc.pid
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

if script_pid is None:
    print(f"Could not find process for {script_to_monitor}")
    exit()

# Join :- @JAVAxCheaT # Monitor the script
while True:
    try:
        # Join :- @JAVAxCheaT # Check if the script is still running
        proc = psutil.Process(script_pid)
        if not proc.is_running():
            # Join :- @JAVAxCheaT # If the script is not running, send the command to the terminal
            subprocess.run(command, shell=True)

            # Join :- @JAVAxCheaT # Wait for 10 seconds before checking again
            time.sleep(10)

            # Join :- @JAVAxCheaT # Get the new process ID of the script
            script_pid = None
            for proc in psutil.process_iter():
                try:
                    if proc.name() == 'python' and any(script_to_monitor in part for part in proc.cmdline()):
                        script_pid = proc.pid
                        break
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            if script_pid is None:
                print(f"Could not find process for {script_to_monitor}")
                exit()
    except psutil.NoSuchProcess:
        # Join :- @JAVAxCheaT # If the script process does not exist, send the command to the terminal
        subprocess.run(command, shell=True)

        # Join :- @JAVAxCheaT # Wait for 10 seconds before checking again
        time.sleep(10)

        # Join :- @JAVAxCheaT # Get the new process ID of the script
        script_pid = None
        for proc in psutil.process_iter():
            try:
                if proc.name() == 'python' and any(script_to_monitor in part for part in proc.cmdline()):
                    script_pid = proc.pid
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        if script_pid is None:
            print(f"Could not find process for {script_to_monitor}")
            exit()