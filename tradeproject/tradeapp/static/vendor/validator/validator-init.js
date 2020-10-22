
$(function () {
    $(".currency_validate").validate({
        rules: {
            firstname: "required",
            lastname: "required",
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 5
            },
            currency: {
                required: true
            },
            currency_amount: {
                required: true
            },
            usd_amount: {
                required: true
            },
            method: {
                required: true
            }
        },
        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            email: "Please enter a valid email address"
        },
    });
});

$(function () {
    $(".currency2_validate").validate({
        rules: {
            firstname: "required",
            lastname: "required",
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 5
            },
            currency: {
                required: true
            },
            currency_amount: {
                required: true
            },
            usd_amount: {
                required: true
            },
            method: {
                required: true
            }
        },
        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            email: "Please enter a valid email address"
        },
    });
});

$(function () {
    $(".contact_validate").validate({
        rules: {
            firstname: "required",
            lastname: "required",
            email: {
                required: true,
                email: true
            },
            message: "required",
        },
        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            email: "Please enter a valid email address"
        },
    });
});

$(function () {
    $(".signin_validate").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 5
            },
        },
        messages: {
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            email: "Please enter a valid email address"
        },
    });
});

$(function () {
    $(".signup_validate").validate({
        rules: {
            username: "required",
            fullname:{

              required: true,
            },
            email: {
                required: true,
                email: true
            },

            number: {
                required: true,
                minlength: 11,
                maxlength: 11

            },

            password: {
                required: true,
                minlength: 5
            },


        },
        messages: {
          username: "Please enter your username",
          fullname: "Please enter your fullname",
            number: "Please enter a valid number",
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            email: "Please enter a valid email address"
        },
    });
});

$('#confirm_password').keyup(function functionName() {

  if ($(this).val() ==$('#first_password').val()) {

    $('.sign_up').show()

  }

  else {
    $('.sign_up').hide()
  }

})


$('.sign_up').hide()

$(function () {
    $(".personal_validate").validate({
        rules: {
            fullname: "required",
            dob: "required",
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 5
            },
            presentaddress: "required",
            permanentaddress: "required",
            city: "required",
            postal: "required",
            country: {
                required: true
            }
        },
        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            email: "Please enter a valid email address"
        },
    });
});
