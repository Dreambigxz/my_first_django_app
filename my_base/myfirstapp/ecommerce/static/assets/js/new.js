// csrf token for post request

function getToken(name) {
   var cookieValue = null;
   if (document.cookie && document.cookie !== '') {
       var cookies = document.cookie.split(';');
       for (var i = 0; i < cookies.length; i++) {
           var cookie = cookies[i].trim();
           // Does this cookie string begin with the name we want?
           if (cookie.substring(0, name.length + 1) === (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
           }
       }
   }
   return cookieValue;
}

// checking variables

var csrftoken = getToken('csrftoken')

console.log(csrftoken)
console.log(process_deposit);
console.log($('#deposit_amount').val())


var email= user_email
var name= user_full_name
var id= user_id
var phone= user_phone


// hide deposit butoon



// display if amount is greater than or equall 100
$(document).ready(function()
  {
    $("#deposit_amount").on("keyup",function (event) {

   if ($(this).val() >= 100){
       console.log($(this).val())
      $('button.submitt_billing').show()
   }

   else if ($(this).val() <= 99) {
     $('button.submitt_billing').hide()

   }
   else {
     $('button.submitt_billing').hide()
   }

   console.log( $(this).val() );
 });
});


//$('button#depositpaymentbtn').click(function functionName() {
//  FlutterwaveCheckout({
//    public_key: "FLWPUBK_TEST-ad745b9b6ef96bf9f1b2834ac7fbc73a-X",
//    tx_ref:deposit_ref,
//    amount: $('#deposit_amount').val(),
//    currency: "NGN",
//    payment_options: "card, mobilemoneyghana, ussd",
//    /*redirect_url: // specified redirect URL
//      "https://callbacks.piedpiper.com/flutterwave.aspx?ismobile=34",*/
//    meta: {
//      consumer_id: user_id,
//      consumer_mac: "92a3-912ba-1192a",
//    },
//    customer: {
//      email: user_email,
//      phone_number: user_phone,
//      name: user_full_name,
//    },
//
//    callback: function (data) {
//            var obj = JSON.stringify(data)
//            console.log(obj);
//            console.log('this is ' + obj);
//
//            $.ajax({
//
//              type: 'POST',
//              headers:{
//                        'Content-Type':'application/json',
//                        'X-CSRFToken':csrftoken,
//                        },
//              url: process_deposit,
//              data:JSON.stringify({'data':data})
//
//
//            })
//
//
//          var obj = data
//
//          if (obj.status=='successful'){
//
//            location.reload()
//
//             console.log('TRUE')
//          }
//          else{
//              console.log('False')
//          }
//
//    },
//
//
//    onclose: function() {
//
//      window.location.href = '/user_wallet'
//      // close modal
//    },
//
//
//    customizations: {
//      title: "Deposit",
//      description: "Funding wallet",
//      logo: "https://assets.piedpiper.com/logo.png",
//    },
//  });
//
//})



 //adjax call on add to cart button on product page
function functionName() {
  console.log(2*2);
}


 $('.color').click(function Getcolor(e){
                   e.preventDefault();
                   var color= ($(this).text())

                  console.log(color);
})


$('button#addtocartbtn').click(function functionName(e) {
 e.preventDefault();

 // console.log('ccc');
 //
 // var dcolor= color
 // console.log('checkin'+ dcolor);



$.ajax({

 type: 'GET',
 url: proces_add_to_cart,
 data: {'color': 'dcolor'},
 dataType: 'json',

 success: function functionName(data) {


   if ( data.added) {
     console.log(data);



     const total = data.added[1]
       var products = data.added[2]
       console.log(total)

         $("#totalcart").html(total)
         $("#totalcartx").html(total)
         $("#snackbar").html(products + ' added to cart')


         var x = document.getElementById("snackbar");
         x.className = "show";
         setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);

   }

   else if (data.inc) {

     console.log(data);



       const total = data.inc[1]
       const product= data.inc[2]
       console.log(total);
       console.log(product);
       // console.log(product);

       $("#totalcart").html(total)
       $("#totalcartx").html(total)
       $("#snackbar2").html(product + ' updated successfully')

         var x = document.getElementById("snackbar2");
         x.className = "show";
         setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);



   }
   else {
     data.ananymous
     alert(' Anannymous user add to cart pending');
   }


 }

})

})

$('#tag').click(function functionName() {

  console.log($(this).text());

})

//on close of add to cart modal refresh the page
$('button.close').click(function functionName() {

  location.reload()
  console.log('click');

})


var x = document.getElementById("revmess");
x.className = "show";
setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
