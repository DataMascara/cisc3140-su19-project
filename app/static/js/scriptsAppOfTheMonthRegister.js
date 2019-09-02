// 'validateEmail' checks if the email is of the form: what@email.com
function validateEmail()
{
    var email = document.getElementsByClassName("email")[0];
    //alert(email.value);
    if(!email.value.match(/(.*)@(.*)\.(.+)(.+)(.+)/))
        email.setCustomValidity("Email is not of the form what@email.com");
    else
        email.setCustomValidity("");
}

// 'validateNames' checks if the first name and the last name are only of alphabetic chatacters.
function validateNames(object)
{
    object.value = object.value.replace(/[^a-zA-Z]+/g,""); // Erase all the non-alphabetic chars.
}


// Make Received URLs no longer than 300 chars:
function URLLength ()
{
     if (document.getElementsByClassName("addimage")[0].value.length > 0)
     {
          document.getElementsByClassName("addimage")[0].required = true;
          if (document.getElementsByClassName("addimage")[0].value.length > 300)
               document.getElementsByClassName("addimage")[0].setCustomValidity("URL must be no longer than 300 chars!");
          else
               document.getElementsByClassName("addimage")[0].setCustomValidity("");
     }
     else
          document.getElementsByClassName("addimage")[0].required = false;
}

