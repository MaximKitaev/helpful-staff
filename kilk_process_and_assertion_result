def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode(encoding="utf8",errors='ignore')
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


def kill_process(process_name):
    subprocess.Popen(f"taskkill /f /im {process_name}")
    assert not process_exists('firefox.exe'), 'Firefox Process Wasnt Closed'


proc = 'firefox.exe'
kill_process(proc)
assert not process_exists(proc), 'Error. Process Process Wasnt Closed'
