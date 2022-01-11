$(document).ready(function () {

  $(".form-control").on('input', function () {
    var quantity = parseInt($("#id_quantity").val());
    var dv = parseFloat($("#id_dv").val());
    var usd = parseFloat(quantity * dv).toFixed(2);
    $("#id_importValueUSD").val(usd);

    var exrate = parseFloat($("#id_exRate").val());
    var pkr0 = parseFloat(usd * exrate);
    var pkr = Math.round(pkr0)
    $("#id_pkr").val(pkr);

    var ins = parseFloat($("#id_insurance").val());
    var importvalue1 = parseFloat(usd * exrate) + ins;
    var onepercent = Math.round(importvalue1 * 0.01);
    var importvalue2 = Math.round(importvalue1 + onepercent);
    $("#id_importValue").val(importvalue2);
    $("#id_landingCharges").val(onepercent);

    

    // Excise

    if (quantity <= 1250) {
      var excise = (importvalue2 * 0.0120) + 1000;
      $("#id_excise").val(Math.round(excise));
    }
    else if (quantity > 1250 && quantity <= 2030) {
      var excise = (importvalue2 * 0.0121) + 1000;
      $("#id_excise").val(Math.round(excise));
    }
    else if (quantity > 2030 && quantity <= 4060) {
      var excise = (importvalue2 * 0.0122) + 1000;
      $("#id_excise").val(Math.round(excise));
    } 
    else if (quantity > 4060 && quantity <= 8120) {
      var excise = (importvalue2 * 0.0123) + 1000;
      $("#id_excise").val(Math.round(excise));
    } 
    else if (quantity > 8120 && quantity <= 16000) {
      var excise = (importvalue2 * 0.0124) + 1000;
      $("#id_excise").val(Math.round(excise));
    }
    else if (quantity > 16000) {
      var excise = (importvalue2 * 0.0125) + 1000;
      $("#id_excise").val(Math.round(excise));
    }  
    else {
      
    }
    
    

    //Custom Duty

    if ($("#id_dutyType").val() == "F") {
      var rcd = parseFloat($("#id_rateOfDuty").val());
      var quantityInTon = quantity / 1000
      var cd = Math.round(quantityInTon * rcd);
      $("#id_customDuty").val(cd);

    } else if ($("#id_dutyType").val() == "%") {
      var rcd = parseFloat($("#id_rateOfDuty").val());
      var cd = Math.round(importvalue2 * (rcd / 100));
      $("#id_customDuty").val(cd);
      //alert("DUTY TYPE IS Percent");
    } else {
      
    }

    // Additional Custom Duty
    var racd = parseFloat($("#id_rateOfAddDuty").val());
    var acd = Math.round(importvalue2 * (racd / 100));
    $("#id_addCustomDuty").val(acd);

    //Sales Tax
    var ica = Math.round(importvalue2 + cd + acd);
    var rst = parseFloat($("#id_rateOfST").val());
    var st = Math.round(ica * (rst / 100));
    $("#id_salesTax").val(st);

    //Sales Tax
    var icas = Math.round(importvalue2 + cd + acd + st);
    var rit = parseFloat($("#id_rateOfIT").val());
    var it = Math.round(icas * (rit / 100));
    $("#id_incomeTax").val(it + 26);

    //CESS
    var quantityInTon = quantity / 1000;
    var rateOfCess = parseInt($("#id_rateOfCess").val());
    var cess = Math.round(quantityInTon * rateOfCess)
    $("#id_cess").val(cess);

    //RD
    var rateOfRD = parseFloat($("#id_rateOfRD").val())
    var rd = Math.round(importvalue2 * (rateOfRD / 100))
    $("#id_rd").val(rd)

    //Anti Dumping
    var rateOfAD = parseFloat($("#id_rateOfAD").val())
    var ad = Math.round(importvalue2 * (rateOfAD / 100))
    $("#id_antiDumping").val(ad)

    //TOTAL
    //var total = parseInt(cd) + parseInt(acd) + parseInt(st) + parseInt(it) + parseInt(Number(cess)) + parseInt(Number(rd)) + parseInt(Number(ad));
    
    var total = Number($("#id_customDuty").val())+
                Number($("#id_addCustomDuty").val())+
                Number($("#id_salesTax").val())+
                Number($("#id_incomeTax").val())+
                Number($("#id_cess").val())+
                Number($("#id_rd").val())+
                Number($("#id_antiDumping").val())
    
    //document.getElementById('#id_total').value = total + 26;

  });


});
