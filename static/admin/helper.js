function Print_received(message) {
    message = "> " + message;
    $("#ms-output").text(
        $("#ms-output").text() +
        message +
        "\n"
    );
}

function Print_sent(message) {
    message = "< " + message;
    $("#ms-output").text(
        $("#ms-output").text() +
        message +
        "\n"
    );
}

let url = "ws://localhost:8888/adminWS";
webSocket = new WebSocket(url);

function wsSetup() {

    webSocket.onopen = function (event) {
        webSocket.send(
            JSON.stringify({
                to : "-1",
                message : "connection established"
            })
        );
        Print_sent("connection established");
    }

    webSocket.onmessage = function (event) {
        let dt = event.data;
        if (dt == "#close") {
            webSocket.close();
            Print_received("connection closed");
        } else {
            Print_received(dt);
        }
    }

    webSocket.onclose = function (event) {
        Print_received("connection closed by server");
    }
}

function dropdown() {
    $("a.dropdown-item").on("click", function(e) {
        e.preventDefault();
        $("#user-dropdown").text(this.text);
        $('#btn-send').removeClass("disabled");
        $("input[type=text]").attr("readonly", false);
    });
}