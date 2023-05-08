import psutil
import platform
import cpuinfo

# CPU information
print("CPU cores:", psutil.cpu_count())
print("Operating System Version :", platform.platform())
print("System Name:", platform.node())

my_cpu_info = cpuinfo.get_cpu_info()
print("Full CPU Name:", my_cpu_info['brand_raw'])


# Memory information
mem = psutil.virtual_memory()
print(f"Total memory: {mem.total / (1024 ** 3):.2f} GB")
print(f"Available memory: {mem.available / (1024 ** 3):.2f} GB")

# Disk information
disk = psutil.disk_usage("/")
print(f"Total disk space: {disk.total / (1024 ** 3):.2f} GB")
print(f"Used disk space: {disk.used / (1024 ** 3):.2f} GB")
print(f"Free disk space: {disk.free / (1024 ** 3):.2f} GB")

