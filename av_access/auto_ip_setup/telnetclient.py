import asyncio
import telnetlib3
import sys

PASSWORD = "root"
BUF_SIZE =  4096

def get_new_ip_address():
    return sys.argv[2] 

async def shell(reader,writer):

    outp = await reader.read(BUF_SIZE)
    print("Not Av Access sent: ", repr(outp))

    writer.write(f"{PASSWORD}\r\n")
    await writer.drain()
    print(f"Client sent: {PASSWORD}")

    response = await reader.read(BUF_SIZE)
    print("Server replied: ", repr(response))
    outp = await reader.read(BUF_SIZE)
    print("Not Av Access sent: ", repr(outp))

    writer.write("gbparam s ip_mode \"static\"\r\n")
    await writer.drain()
    print("\nClient sent: gbparam s ip_mode \"static\"\r\n")

    response = await reader.read(BUF_SIZE)
    print("Server replied: ", repr(response))
    outp = await reader.read(BUF_SIZE)
    print("Not Av Access sent: ", repr(outp))

    writer.write(f"gbparam s ipaddr {get_new_ip_address()}\r\n")
    await writer.drain()
    print(f"\nClient sent: gbparam s ipaddr {get_new_ip_address()}\"\r\n")

    response = await reader.read(BUF_SIZE)
    print("Server replied: ", repr(response))
    outp = await reader.read(BUF_SIZE)
    print("Not Av Access sent: ", repr(outp))

    writer.write("gbparam s netmask 255.255.255.0\r\n")
    await writer.drain()
    print("\nClient sent: gbparam s netmask 255.255.255.0\"\r\n")

    response = await reader.read(BUF_SIZE)
    print("Server replied: ", repr(response))
    outp = await reader.read(BUF_SIZE)
    print("Not Av Access sent: ", repr(outp))

    writer.write("reboot\r\n")
    await writer.drain()
    print("\nClient sent: reboot\"\r\n")

    response = await reader.read(BUF_SIZE)
    print("Server replied: ", repr(response))
    outp = await reader.read(BUF_SIZE)
    print("Not Av Access sent: ", repr(outp))


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