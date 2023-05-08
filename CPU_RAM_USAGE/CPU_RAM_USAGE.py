import psutil

# Get CPU usage as a percentage
cpu_usage_percent = psutil.cpu_percent()

# Get memory usage in bytes and convert to MB
memory_usage = psutil.virtual_memory().used / (1024 ** 2)

# Print results
print(f"CPU usage: {cpu_usage_percent}%")
print(f"Memory usage: {memory_usage:.2f} MB")
