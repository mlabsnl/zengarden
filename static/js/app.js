/**
 * jQuery.ajax mid - CROSS DOMAIN AJAX 
 * ---
 * @author James Padolsey (http://james.padolsey.com)
 * @version 0.11
 * @updated 12-JAN-10
 * ---
 * Note: Read the README!
 * ---
 * @info http://james.padolsey.com/javascript/cross-domain-requests-with-jquery/
 */


jQuery.extend(jQuery.validator.messages, {
        required: "&larr; verplicht.",
        remote: "Controleer dit veld.",
        email: "&larr; Vul hier een geldig e-mailadres in.",
        url: "Vul hier een geldige URL in.",
        date: "Vul hier een geldige datum in.",
        dateISO: "Vul hier een geldige datum in (ISO-formaat).",
        number: "&larr; Vul hier een geldig getal in.",
        digits: "Vul hier alleen een getal in.",
        creditcard: "Vul hier een geldig creditcardnummer in.",
        equalTo: "Vul hier dezelfde waarde in.",
        accept: "Vul hier een waarde in met een geldige extensie.",
        maxlength: jQuery.validator.format("Vul hier maximaal {0} tekens in."),
        minlength: jQuery.validator.format("Vul hier minimaal {0} tekens in."),
        rangelength: jQuery.validator.format("Vul hier een waarde in van minimaal {0} en maximaal {1} tekens."),
        range: jQuery.validator.format("&larr; Vul hier een waarde in van minimaal {0} en maximaal {1}."),
        max: jQuery.validator.format("Vul hier een waarde in kleiner dan of gelijk aan {0}."),
        min: jQuery.validator.format("&larr; Vul hier een waarde in groter dan of gelijk aan {0}.")
});
 
            $(function () {
			
			
			
			
			var prijsRustgever = 24.95;
			var prijsVerzendkosten = 2.55;
			var totaalprijs;
			var aantal;
			
	
              $("a[rel=popover]")
                .popover({
                  offset: 10
                })
                .click(function(e) {
                  e.preventDefault()
                })



				function validateform() {
					$("#bestelformulier").validate({
					  rules: {
					    product_amount: {
					      digits: true,
					      min: 1
					    },
						customer_name: {
							required: true
						},
						customer_street: {
							required: true
						},
						customer_number: {
							required: true
						},
						customer_zipcode: {
							required: true
						},
						customer_city: {
							required: true
						},
						customer_email: {
							required: true,
							email: true	
						}
						
					
					  }
					});
					
						aantal = parseFloat($("#id_product_amount").val())
						origineleprijs = (aantal * prijsRustgever) + prijsVerzendkosten;
						totaalprijs = Math.round( origineleprijs *100)/100
						$("#totaalprijs").html( totaalprijs.toFixed(2))

						if ($("#bestelformulier").valid() ) {
						   	$("a#bestelknop").removeClass("disabled").attr("href","#")

						} else {
							$("a#bestelknop").addClass("disabled").attr("href","#")
						}
					
					
				}
				$("#bestelformulier input").blur(function() {
					
					validateform();

				})
		
				
				$("#sluitvoorwaarden").click(function() {
					$('#voorwaarden').modal('hide')
				})

                $("#bestelknop").click(function(){
                    $('#bestelformulier').submit()
                })

            })
         