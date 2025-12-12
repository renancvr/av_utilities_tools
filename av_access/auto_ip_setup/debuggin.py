import asyncio
import telnetlib3
import sys

PASSWORD = "root"

def get_new_ip_address():
    return sys.argv[2] 

async def shell(reader,writer):

    outp = await reader.read(1024)
    print("Not Av Access sent: ", repr(outp))

    writer.write(f"{PASSWORD}\r\n")
    await writer.drain()
    print(f"Client sent: {PASSWORD}")

    response = await reader.read(1024)
    print("Server replied: ", repr(response))
    outp = await reader.read(1024)
    print("Not Av Access sent: ", repr(outp))

    writer.write(f"reboot")
    await writer.drain()
    print(f"Client sent: reboot\r\n")

    response = await reader.read(1024)
    print("Server replied: ", repr(response))

    outp = await reader.read(1024)
    print("Not Av Access sent: ", repr(outp))

    outp = await reader.read(1024)
    print("Not Av Access sent: ", repr(outp))

    outp = await reader.read(1024)
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

    if len(sys.argv) > 1:
        old_ip_addr = sys.argv[1]
        asyncio.run(main(old_ip_addr))