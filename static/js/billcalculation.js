$(document).ready(function(){
    
    $("form").on('input', function (){
        
            var total = 0;
            $('.by-us').each(function(){
               total += Number($(this).val());
               $("#id_grossTotal").val(total);
        });
        
        var grossTotal = parseInt($("#id_grossTotal").val())
        var charges = parseInt($("#id_charges").val())
        var rateOfST = parseInt($("#id_rateOfST").val())
        var st = (charges * rateOfST) / 100;
        $("#id_salesTax").val(st)

        var totalAmount = grossTotal + charges + st;
        console.log(totalAmount);
        $("#id_total").val(totalAmount);
        });


});
            