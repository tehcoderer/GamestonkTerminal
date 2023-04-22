import json

from websockets import exceptions
from websockets.server import WebSocketServerProtocol, serve

from openbb_terminal.base_helpers import console
from openbb_terminal.stocks.stocks_helper import display_candle, load


class SDKWebSocket:
    def __init__(self, port: int = 9999):
        self.port = port

    async def start_websocket(self, port: int):
        """Start the websocket server."""
        start_server = serve(
            self.websocket_handler,
            "localhost",
            port,
            ssl=None,
        )
        async with start_server:
            await asyncio.Future()

    async def websocket_handler(self, websocket: WebSocketServerProtocol):
        """Handle the websocket connection."""
        async for message in websocket:
            try:
                data = json.loads(message)
                if data["type"] == "sdk":
                    console.print(f"[bold green]Websocket request:[/] {data['ticker']}")
                    data = load(data["ticker"]).to_json(
                        orient="split", date_format="iso"
                    )

                    sdk_data = {"type": "sdk", "data": json.dumps(json.loads(data))}

                    await websocket.send(json.dumps(sdk_data))
                elif data["type"] == "auth" and data["token"] == "SEXY_TOKEN":
                    await websocket.send("AUTHENTICATED")
                elif data["type"] == "ticker":
                    console.print(f"[bold green]Websocket request:[/] {data['ticker']}")
                    figure = display_candle(data["ticker"], external_axes=True)
                    data = json.loads(figure.to_json())
                    sdk_data = {"type": "plotly", "data": json.dumps(data)}
                    await websocket.send(json.dumps(sdk_data))

            except exceptions.ConnectionClosedError:
                pass
            except exceptions.ConnectionClosedOK:
                pass


async def main():
    sdk_websocket = SDKWebSocket()
    await sdk_websocket.start_websocket(9999)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
