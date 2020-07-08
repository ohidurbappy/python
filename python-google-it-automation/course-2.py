import shutil
import psutil






du=shutil.disk_usage("/")
free_space=(du.free/du.total)*100
print("----------Stats---------")

print("Free Space: {free_space:.2f}%".format(free_space=free_space))

cu=psutil.cpu_percent(0.1)

print(cu)