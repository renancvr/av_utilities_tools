import asyncio
import telnetlib3
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

async def shell(reader, writer):
    addr = writer.get_extra_info("peername")
    logging.info(f"Client connected: {addr}")

    try:
        writer.write("This is not an Av Access device. Type 'exit' to quit.\r\nNotAvAccess> ")
        await writer.drain()

        async for line in reader:
            line = line.rstrip("\r\n")
            logging.info(f"Received: {line!r} from {addr}")

            if line.lower() == "exit":
                writer.write("Bye.\r\n")
                await writer.drain()
                break

            writer.write(f"{line}\r\nNotAvAcess> ")
            await writer.drain()

    except Exception as e:
        logging.exception(f"Error in shell: {e}")
    finally:
        logging.info(f"Closing connection to {addr}")
        writer.close()


async def main():
    server = await telnetlib3.create_server(
        host="127.0.0.1",
        port=24,
        shell=shell,
        encoding="utf8",
    )
    logging.info("Not an Av Access listening on 127.0.0.1:24")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())