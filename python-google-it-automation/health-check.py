import shutil
import psutil
import requests
import socket

def check_disk_usage(disk):
    du=shutil.disk_usage(disk)
    disk_free=(du.free/du.total)*100
    return disk_free>20


def check_cpu_usage(second):
    cu=psutil.cpu_percent(second)
    return cu<75


def check_localhost():
    localhost=socket.gethostbyname('localhost')
    return localhost=='127.0.0.1'

def check_connectivity():
    response=requests.head("http://www.google.com")
    return response.status_code==200


if __name__ == "__main__":
    if check_disk_usage("/"):
        print("Disk : OK")
    else:
        print("Disk: Not OK")

    if check_cpu_usage(1):
        print("CPU: OK")

    else:
        print("CPU: Not OK")

    if check_localhost():
        print("Localhost OK")

    if check_connectivity():
        print("Internet Connectivity OK!")

