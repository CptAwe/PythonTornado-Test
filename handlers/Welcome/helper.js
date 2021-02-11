function Print(message) {
    message = "> " + message;
    $("#ms-output").text(message);
}

function wsSetup() {

    let url = "ws://localhost:8888/start";

    webSocket = new WebSocket(url);

    webSocket.onopen = function(event) {
        webSocket.send("connection established");
    }

    webSocket.onmessage = function(event) {
        let dt = event.data;
        if (dt == "#close"){
            webSocket.close();
        } else {
            Print(dt);
        }
    }
}