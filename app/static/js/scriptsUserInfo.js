/* JavaScript file for: 'userInfo.html'
    version 1.1
    08.13.2019
    Description: `subscribePortIndex` function added
    
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

// Change the color of the subscription button and what is written on it if it is pressed. Then, submit the form:
function subscribePortIndex(object)
{
    // Extraction of the 'id' of the port:
    var id = object.className.substr(24);

    var subscribeButton = document.getElementsByClassName("subscribe" + id)[0];
 
   if (subscribeButton.value ==  'Subscribe')
   {
       subscribeButton.style.backgroundColor = '#7B2240'; // It means the user is subscribed to the particular port. Color the calling button maroon, and
       subscribeButton.value = 'Joined'; // Change the text on the button to 'Joined'.
       subscribeButton.title = 'Joined'; // Change the title text on the button to 'Joined'.
   }
   else // Otherwise, if the user clicked again (to unsubscribe):
   {
       subscribeButton.style.backgroundColor = 'rgb(117, 117, 117)'; // Turn the color back to gray,
       subscribeButton.value = 'Subscribe'; // Change the text on the button to 'Subscribe'.
       subscribeButton.title = 'Subscribe'; // Change the title text on the button to 'Subscribe'.
   }

   // Now check if this port is also in the 'trending ports' section, and change the color of the button accordingly:
   for (i = 0; i < document.getElementsByClassName("trendingName").length; i++)
   {
        if (document.getElementsByClassName("trendingName")[i].innerHTML == document.getElementsByClassName("portName" + id)[0].innerHTML)
        {
                // Note that the index below is 'i-1'. The reason is that we enumerate the 'trending ports' starting from 1 and not from ,
                // which is why here we have to subtract 1 to get to the right button!
                document.getElementsByClassName("subscribe")[i-1].style.backgroundColor = subscribeButton.style.backgroundColor;
                document.getElementsByClassName("subscribe")[i-1].value = subscribeButton.value;
                document.getElementsByClassName("subscribe")[i-1].title = subscribeButton.title;
        }
   }

   document.getElementsByClassName("subscriptionForm" + id)[0].submit(); // Now submit this information
}
