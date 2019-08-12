var first_name = document.getElementById("first_name");
var last_name = document.getElementById("last_name");
var username = document.getElementById("username");
var email = document.getElementById("email");
var password = document.getElementById("password");
var confirm_password = document.getElementById("confirm_password");

function validatePassword()
{
    if(password.value != confirm_password.value)
    {
        confirm_password.setCustomValidity("Passwords Don't Match");
        confirm_password.reportValidity();
    }
    else if(password.value.trim() == "")
    {
        password.setCustomValidity("Passwords must not be empty");
        password.reportValidity();
    } else
    {
        password.setCustomValidity("");
    }
}
password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;
