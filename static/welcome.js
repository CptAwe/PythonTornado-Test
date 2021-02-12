$( function() {

    wsSetup();

    $("#btn-send").on("click", function(e) {
        e.preventDefault();
        let message = $("input[type=text]").val();
        console.log(message);
        webSocket.send(message);
        Print_sent(message);
    });

});

