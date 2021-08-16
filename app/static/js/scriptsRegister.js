﻿// 'validatePassword' ensures passwords of more than 6 characters long and matching between them.
function validatePassword()
{
    var password = document.getElementsByClassName("password")[0];
    var confirm_password = document.getElementsByClassName("confirm_password")[0];

    if (password.value.length < 7 || password.value.length > 128)
    {
        password.setCustomValidity("Passwords must be between 7 and 128 characters!");
    }
    else if (confirm_password.value.length < 7 || confirm_password.value.length > 128)
    {
        password.setCustomValidity("");
        confirm_password.setCustomValidity("Passwords must be between 7 and 128 characters!");
    }
    else if(password.value != confirm_password.value)
    {
        password.setCustomValidity("");
        confirm_password.setCustomValidity("Passwords don't match!");
    }
    else
    {
        confirm_password.setCustomValidity("");
        password.setCustomValidity("");
    }
}

// 'validateUserNameLength' checks if the username is more than 6 characters long.
function validateUserNameLength()
{
    var username = document.getElementsByClassName("usernameForm")[0];

    if(username.value.length < 7)
        username.setCustomValidity("Username must be of at least 7 characters!");
    else if (username.value.length > 30)
        username.setCustomValidity("Username must be of at most 30 characters!");
    else
        username.setCustomValidity("");
}

// 'validateNames' checks if the first name and the last name are at most 30 chars.
function validateNames(object)
{
    object.value = object.value.replace(/[^a-zA-Z]+/g,""); // Erase all the non-alphabetic chars.
    if(object.value.length > 30)
        object.setCustomValidity("A name must be of at most 30 characters!");
    else
        object.setCustomValidity("");
}

// 'validateEmail' checks if the email is of the form: what@email.com
function validateEmail()
{
    var email = document.getElementsByClassName("email")[0];
    //alert(email.value);
    if(!email.value.match(/(.*)@(.*)\.(.+)(.+)(.+)/))
        email.setCustomValidity("Email is not of the form what@email.com");
    else if (email.value.length > 128)
        email.setCustomValidity("Email must be of at most 128 characters!");
    else
        email.setCustomValidity("");
}

// A function writing the name of the uploaded file in the place of the "Add Image" button:
function changeVal ()
{
       if (document.getElementsByClassName("imageUpload")[0].value != '')
       	document.getElementsByClassName("imageLabel")[0].innerHTML = document.getElementsByClassName("imageUpload")[0].value;
       else
                 document.getElementsByClassName("imageLabel")[0].innerHTML = "Your Image";
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
