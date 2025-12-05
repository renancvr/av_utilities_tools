import pandas as pd
import sys
import os
import time

def config_manual():

    total_devices = int(input("Total of encoders/decoders: "))

    for i in range(total_devices):
        print(f"Device {i+1}")
        old_ip_addr = input("Old IP Address: ")
        new_ip_addr = input("New IP Address: ")

        os.system(f"python telnetclient.py {old_ip_addr} {new_ip_addr}")

def config_via_sheet():

    file_path = sys.argv[1]

    df = pd.read_excel(file_path)

    ips = df.values.tolist()


    for ip in ips:

        old_ip_addr = ip[0]
        new_ip_addr = ip[1]

        print(f"Changing ip {old_ip_addr} to {new_ip_addr}")
        for i in range(50):
            print('#', end='',flush=True)
            time.sleep(0.03)
        print('\n')


        os.system(f"python telnetclient.py {old_ip_addr} {new_ip_addr}")

if __name__ == "__main__":

    if len(sys.argv) > 1:
        config_via_sheet()
    else:
        config_manual()
