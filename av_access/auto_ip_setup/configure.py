import pandas as pd
import sys
import time
import subprocess

def run_client(old_ip_addr,new_ip_addr):

    result = subprocess.run(
        ["python","telnetclient.py",old_ip_addr,new_ip_addr]
    )

    if result.returncode != 0:
        print(f"\n[ERROR] telnet client failed for {old_ip_addr}\n")
    else:
        print(f"\n[OK] {old_ip_addr} updated to {new_ip_addr}\n")

def config_manual():

    total_devices = int(input("Total of encoders/decoders: "))

    for i in range(total_devices):
        print(f"Device {i+1}")
        old_ip_addr = input("Old IP Address: ")
        new_ip_addr = input("New IP Address: ")

        run_client(old_ip_addr,new_ip_addr)

def config_via_sheet():

    file_path = sys.argv[1]

    df = pd.read_excel(file_path)

    ips = df.values.tolist()


    for ip in ips:

        old_ip_addr = ip[0]
        new_ip_addr = ip[1]

        print(f"Changing ip {old_ip_addr} to {new_ip_addr}")
        for i in range(100):
            print('#', end='',flush=True)
            time.sleep(0.015)
        print()

        run_client(old_ip_addr,new_ip_addr)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        config_via_sheet()
    else:
        config_manual()
