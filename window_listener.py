import win32con, win32api, win32gui, ctypes, ctypes.wintypes,time

class COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ('dwData', ctypes.wintypes.LPARAM),
        ('cbData', ctypes.wintypes.DWORD),
        ('lpData', ctypes.c_void_p)
    ]

PCOPYDATASTRUCT = ctypes.POINTER(COPYDATASTRUCT)

class Listener:
    def create_window(self):
        print('creating new listener for proxy soft...')
        message_map = {
            win32con.WM_COPYDATA: self.OnCopyData
        }
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = message_map
        wc.lpszClassName = 'MyWindowClass'
        hinst = wc.hInstance = win32api.GetModuleHandle(None)
        classAtom = win32gui.RegisterClass(wc)
        self.classAtom = classAtom
        self.hinst = hinst
        self.hwnd = win32gui.CreateWindow(
            classAtom,
            "win32gui test",
            0,
            0,
            0,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            0,
            0,
            hinst,
            None
        )
        return self.hwnd

    def OnCopyData(self, hwnd, msg, wparam, lparam):
        pCDS = ctypes.cast(lparam, PCOPYDATASTRUCT)
        self.my_data = ctypes.string_at(pCDS.contents.lpData)
        print('received msg from proxy soft:\n', self.my_data)
        return

    def wait_for_msg(self, timeout=30):
        print(f'waiting {timeout} seconds for proxy-soft answer...')
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            win32gui.PumpWaitingMessages()
        self.OnClose()

    def OnClose(self):
        win32gui.DestroyWindow(self.hwnd)
        wc = win32gui.WNDCLASS()
        classAtom = win32gui.UnregisterClass(self.classAtom, None)
        
 
 
'''How to use:'''

'''1. Create a new instanse'''
l = Listener()
'''2. Create a Window'''
l.create_window()
'''3. Get HWND'''
HWND = l.hwnd
'''4. Send Some MSG to HWND. And Star to Listener'''
l.wait_for_msg(timeout=60)
'''5. Get Answer'''
answer = l.my_data
print('We Have An Answer!!!:',answer)
