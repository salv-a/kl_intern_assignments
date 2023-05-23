import asyncio
import websockets


async def main():

    async with websockets.connect("ws://localhost:8765") as websocket:  #CONNECTING

        message = input("Enter the message to be sent to server")   #INPUT MSG TO BE SENT TO SERVER
        await websocket.send(message)   #SENDING MSG
        print(f"Sent message: {message}")


        response = await websocket.recv()
        print(f"Received response: {response}")


asyncio.get_event_loop().run_until_complete(main())
