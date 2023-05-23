import asyncio  # for writing asynchronous code
import websockets

#await-to suspend the execution of the function until a message is received/send


async def handle_connection(websocket):
    message = await websocket.recv()  # RECIEVE MSG FROM CLIENT
    print(f"Received message: {message}")

    response = "Message recieved to server"  # SEND RESPONSE TO CLIENT
    await websocket.send(response)
    print(f"Sent response: {response}")


# CREATE WEBSOCKET SERVER
start_server = websockets.serve(handle_connection, "localhost", 8765)

# STARTING SERVER AND WAIT TILL IT IS SETUP
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
