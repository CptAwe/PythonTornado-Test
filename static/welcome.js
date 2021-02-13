$( function() {

    wsSetup();

    $("#btn-send").on("click", function(e) {
        e.preventDefault();
        let message = $("input[type=text]").val();
        if (message == "") {
            message = $("input[type=text]").attr('placeholder');
        }
        webSocket.send(message);
        Print_sent(message);
        $("input[type=text]").val("");
    });

});

