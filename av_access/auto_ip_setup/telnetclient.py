import asyncio
import telnetlib3
import sys


def get_new_ip_address():
    return sys.argv[2] 

async def shell(reader,writer):

    outp = await reader.read(1024)
    print("Not Av Access sent: ", repr(outp))

    writer.write("root\r\n")
    await writer.drain()
    print("Client sent: root")

    response = await reader.read(1024)
    print("Server replied: ", repr(response))

    writer.write("/ # gbparam s ip_mode \"static\"\r\n")
    await writer.drain()
    print("Client sent: / # gbparam s ip_mode \"static\"\r\n")

    response = await reader.read(1024)
    print("Server replied: ", repr(response))

    writer.write(f"/ # gbparam s ipaddr {get_new_ip_address()}\r\n")
    await writer.drain()
    print(f"Client sent: / # gbparam s {get_new_ip_address()}\"\r\n")

    response = await reader.read(1024)
    print("Server replied: ", repr(response))

    writer.write("/ # gbparam s netmask 255.255.255.0\r\n")
    await writer.drain()
    print("Client sent: / # gbparam s netmask 255.255.255.0\"\r\n")

    response = await reader.read(1024)
    print("Server replied: ", repr(response))
    writer.close()
    try:
        await writer.wait.closed()
    except AttributeError:
        pass

async def main(old_ip_addr):

    reader,writer = await telnetlib3.open_connection(
        host = old_ip_addr,
        port = 24,
        shell = shell,
        encoding = "utf8" 
    )

    await writer.protocol.waiter_closed

if __name__ == "__main__":

    if len(sys.argv) > 2:
        old_ip_addr = sys.argv[1]
        asyncio.run(main(old_ip_addr))