$( function() {

    wsSetup();
    dropdown();

    $("#btn-send").on("click", function(e) {
        e.preventDefault();
        let message = $("input[type=text]").val();
        if (message == "") {
            message = $("input[type=text]").attr('placeholder');
        }
        let target = $("#user-dropdown").text();
        webSocket.send(
            JSON.stringify({
                to : target,
                message : message
            })
        );
        Print_sent(message);
        $("input[type=text]").val("");
    });

});

