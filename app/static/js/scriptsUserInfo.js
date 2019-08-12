/* JavaScript file for: 'userInfo.html'
    version 1.0
    08.12.2019
    Description: Creation of File
- Front End Team
*/

// A function writing the name of the uploaded file in the place of the "Add Image" button:
function changeVal ()
{
       if (document.getElementsByClassName("imageUpload")[0].value != '')
       	document.getElementsByClassName("imageLabel")[0].innerHTML = document.getElementsByClassName("imageUpload")[0].value;
       else
                 document.getElementsByClassName("imageLabel")[0].innerHTML = "Upload Avatar";
}

// Open the "Edit Profile" Area
function openEdit()
{
    if (document.getElementsByClassName("pageTitle")[0].innerHTML == "USER PROFILE")
    {
           document.getElementsByClassName("pageTitle")[0].innerHTML = "EDIT PROFILE";
           document.getElementsByClassName("descriptionText")[0].style.display = "none";
           document.getElementsByClassName("descriptionForm")[0].style.display = "inherit";
           document.getElementsByClassName("editProfileBtn")[0].innerHTML = "CANCEL";
    }
    else
    {
           document.getElementsByClassName("pageTitle")[0].innerHTML = "USER PROFILE";
           document.getElementsByClassName("descriptionText")[0].style.display = "inherit";
           document.getElementsByClassName("descriptionForm")[0].style.display = "none";
           document.getElementsByClassName("editProfileBtn")[0].innerHTML = "EDIT PROFILE";
    }
}

// Submit the Bio form
function submitBio()
{
    if (document.getElementsByClassName("descriptionTextArea")[0].innerHTML != document.getElementsByClassName("descriptionText")[0].innerHTML
        || document.getElementsByClassName("imageUpload")[0].value != "")
    document.getElementsByClassName("descriptionForm")[0].submit(); // Submit the form
}

// Submit a 'checkbox' form
function submitCheckboxForm (theForm)
{
    document.getElementsByClassName(theForm)[0].submit(); // Submit the form
}

// Submit the Email form
function submitEmail()
{
    if (document.getElementsByClassName("emailSetting")[0].value.length != 0 ||
         document.getElementsByClassName("emailSetting")[1].value.length != 0)
    document.getElementsByClassName("changeEmailForm")[0].submit(); // Submit the form
}

// 'validateEmail' checks if the email is of the form: what@email.com
function validateEmail(email)
{
    if(!email.value.match(/(.*)@(.*)\.(.+)(.+)(.+)/))
    {
        email.setCustomValidity("Email is not of the form what@email.com");
        email.required = true;
    }
    else if (document.getElementsByClassName("emailSetting")[0].value != document.getElementsByClassName("emailSetting")[1].value)
    {
        document.getElementsByClassName("emailSetting")[0].setCustomValidity("");
        document.getElementsByClassName("emailSetting")[1].setCustomValidity("Passwords don't match!");
    }
    else
    {
         document.getElementsByClassName("emailSetting")[0].setCustomValidity("");
         document.getElementsByClassName("emailSetting")[1].setCustomValidity("");
    }
}

// 'validatePassword' ensures passwords of more than 6 characters long and matching between them.
function validatePassword()
{
    var current_password = document.getElementsByClassName("currentPassword")[0];
    var password = document.getElementsByClassName("passwordSetting")[0];
    var confirm_password = document.getElementsByClassName("passwordSetting")[1];

    if (current_password.value.length < 7)
    {
        password.setCustomValidity("Passwords must be of at least 7 characters!");
    }
    else if (password.value.length < 7)
    {
        current_password.setCustomValidity("");
        password.setCustomValidity("Passwords must be of at least 7 characters!");
    }
    else if (confirm_password.value.length < 7)
    {
        current_password.setCustomValidity("");
        password.setCustomValidity("");
        confirm_password.setCustomValidity("Passwords must be of at least 7 characters!");
    }
    else if(password.value != confirm_password.value)
    {
        current_password.setCustomValidity("");
        password.setCustomValidity("");
        confirm_password.setCustomValidity("Passwords don't match!");
    }
    else
    {
        current_password.setCustomValidity("");
        confirm_password.setCustomValidity("");
        password.setCustomValidity("");
    }
}