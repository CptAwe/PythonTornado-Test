$( function() {

    wsSetup();

    $("#btn-send").on("click", function(e) {
        e.preventDefault();
        console.log($("input[type=text]").val());
    });

});

