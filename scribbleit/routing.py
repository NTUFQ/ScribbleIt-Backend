from channel import routing
from scribble import consumers

channel_routing = [
    routing("websocket.receive", consumer.ws_message),
    routing("websocket.connect", consumers.ws_connect),
    routing("wensocket.disconnect", consumers.ws_disconnect),
]