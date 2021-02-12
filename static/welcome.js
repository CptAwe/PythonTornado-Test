$( function() {

    wsSetup();

    $("#btn-send").on("click", function(e) {
        e.preventDefault();
        let message = $("input[type=text]").val();
        webSocket.send(message);
        Print_sent(message);
    });

});

