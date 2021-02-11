


var ws = new WebSocket("ws://localhost:8888/start");
ws.onopen = function() {
   ws.send("Hello, world");
};
ws.onmessage = function (evt) {
   alert(evt.data);
};