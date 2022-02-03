$(function () {
    $(".quantily").change(function () {
        var qty = $('.quantily').val()
        var option = $('#combo option:selected').val();

        if (qty < 1) {
            $('#total').html("You can't buy less than 1");
        }
        else {
            if (option == "free") {
                if (qty != 1) {
                    $('#total').html("You can only buy one");
                }
                else {
                    $('#total').html("Total: 0 VND");
                }
            }
            else if (option == "paid1") {
                $('#total').html("Total: " + (qty * 5000) + " VND");
            }
            else if (option == "paid2") {
                if (qty != 1) {
                    $('#total').html("You can only buy one");
                }
                else {
                    $('#total').html("Total: " + (qty * 50000) + " VND");
                }
            }
            else if (option == "paid3") {
                $('#total').html("Total: " + (qty * 300000) + " VND");
            }
        }
    });
});

$(function () {
    $("#combo").change(function () {
        var qty = $('.quantily').val()
        var option = $('#combo option:selected').val();

        if (qty < 1) {
            $('#total').html("You can't buy less than 1");
        }
        else {
            if (option == "free") {
                if (qty != 1) {
                    $('#total').html("You can only buy one");
                }
                else {
                    $('#total').html("Total: 0 VND");
                }
            }
            else if (option == "paid1") {
                $('#total').html("Total: " + (qty * 5000) + " VND");
            }
            else if (option == "paid2") {
                $('#total').html("Total: " + (qty * 50000) + " VND");
            }
            else if (option == "paid3") {
                $('#total').html("Total: " + (qty * 300000) + " VND");
            }
        }
    });
});