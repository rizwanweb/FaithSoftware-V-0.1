$(document).ready(function () {
    $(".form-control").on("input", function () { 

        var deposit = parseInt($("#deposit").val())

        var rent = parseInt($("#id_rent").val())
        var damageCharges = parseInt($("#id_damageCharges").val())
        var washingCharges = parseInt($("#id_washingCharges").val())

        if ($("#id_rent") ) {
            
        }

        var refund
        

        $("#id_refundAmount").val(deposit)
     })
});