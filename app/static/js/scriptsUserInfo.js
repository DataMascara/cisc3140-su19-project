/* JavaScript file for: 'userInfo.html'
    version 1.1.1
    08.13.2019
    Description: `subscribePortIndex` was modified to fix the button coordination bug. Bug fixed!
 
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
    else if (email.value.length > 128)
    {
        email.setCustomValidity("Email must be of at most 128 characters!");
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

    if (current_password.value.length < 7 || current_password.value.length > 128)
    {
        password.setCustomValidity("Passwords must be between 7 and 128 characters!");
    }
    else if (password.value.length < 7 || password.value.length > 128)
    {
        current_password.setCustomValidity("");
        password.setCustomValidity("Passwords must be between 7 and 128 characters!");
    }
    else if (confirm_password.value.length < 7 || confirm_password.value.length > 128)
    {
        current_password.setCustomValidity("");
        password.setCustomValidity("");
        confirm_password.setCustomValidity("Passwords must be between 7 and 128 characters!");
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
   for (i = 0; i < document.getElementsByClassName("trendingName").length; i+=2)
   {
        if (document.getElementsByClassName("trendingName")[i].innerHTML == document.getElementsByClassName("portName" + id)[0].innerHTML)
        {
                // Note that the index below is 'i/2'. The reason is that there are two types of objects with the 'trendingName
                // classname, so we 'jump over' the other one.
                document.getElementsByClassName("subscribe")[i/2].style.backgroundColor = subscribeButton.style.backgroundColor;
                document.getElementsByClassName("subscribe")[i/2].value = subscribeButton.value;
                document.getElementsByClassName("subscribe")[i/2].title = subscribeButton.title;
        }
   }

   document.getElementsByClassName("subscriptionForm" + id)[0].submit(); // Now submit this information
}

// Make Received URLs no longer than 300 chars:
function URLLength ()
{
     if (document.getElementsByClassName("avatarURL")[0].value.length > 0)
     {
          document.getElementsByClassName("avatarURL")[0].required = true;
          if (document.getElementsByClassName("avatarURL")[0].value.length > 300)
               document.getElementsByClassName("avatarURL")[0].setCustomValidity("URL must be no longer than 300 chars!");
          else
               document.getElementsByClassName("avatarURL")[0].setCustomValidity("");
     }
     else
          document.getElementsByClassName("avatarURL")[0].required = false;
}

// Submit the Bio form
function submitBio()
{
    URLLength (); // Check this again, just in case the user deleted the field with mouse instead of keyboard.
    if (document.getElementsByClassName("descriptionTextArea")[0].value == document.getElementsByClassName("descriptionText")[0].innerHTML &&
         document.getElementsByClassName("avatarURL")[0].value.length == 0)
    {
         document.getElementsByClassName("descriptionTextArea")[0].required = true;
         document.getElementsByClassName("descriptionTextArea")[0].setCustomValidity("Please fill out this field!");
    }
    else if (document.getElementsByClassName("descriptionTextArea")[0].value.length > 1000)
    {
         document.getElementsByClassName("descriptionTextArea")[0].required = true;
         document.getElementsByClassName("descriptionTextArea")[0].setCustomValidity("Bio can contain at most 1000 chars!");
    }
    else
    {
         document.getElementsByClassName("descriptionTextArea")[0].required = false;
         submitWithEscape ();
         document.getElementsByClassName("descriptionTextArea")[0].setCustomValidity("");
    }
}

// Escape the necessary characters:
function escapeChars (x)
{
    for (i = 0; i < x.value.length; i++)
    {
        if (x.value[i] == "\\")
        {
            if (i != x.value.length-1)
               x.value = x.value.slice(0, i) + "\\\\" + x.value.slice(i+1);
            else
               x.value = x.value.slice(0, i) + "\\\\";
            i++;
        }
        else if (x.value[i] == "\f")
        {
            if (i != x.value.length-1)
               x.value = x.value.slice(0, i) + "\\\f" + x.value.slice(i+1);
            else
               x.value = x.value.slice(0, i) + "\\\f";
            i++;
        }
        else if (x.value[i] == "\r")
        {
            if (i != x.value.length-1)
               x.value = x.value.slice(0, i) + "\\\r" + x.value.slice(i+1);
            else
               x.value = x.value.slice(0, i) + "\\\r";
            i++;
        }
        else if (x.value[i] == "\v")
        {
            if (i != x.value.length-1)
               x.value = x.value.slice(0, i) + "\\\v" + x.value.slice(i+1);
            else
               x.value = x.value.slice(0, i) + "\\\v";
            i++;
        }
        else if (x.value[i] == "\t")
        {
            if (i != x.value.length-1)
               x.value = x.value.slice(0, i) + "\\\t" + x.value.slice(i+1);
            else
               x.value = x.value.slice(0, i) + "\\\t";
            i++;
        }
        else if (x.value[i] == "\0")
        {
            if (i != x.value.length-1)
               x.value = x.value.slice(0, i) + "\\\0" + x.value.slice(i+1);
            else
               x.value = x.value.slice(0, i) + "\\\0";
            i++;
        }
        else if (x.value[i] == "\'")
        {
            if (i != x.value.length-1)
               x.value = x.value.slice(0, i) + "\\\'" + x.value.slice(i+1);
            else
               x.value = x.value.slice(0, i) + "\\\'";
            i++;
        }
    }    
}

// Submit the form w/ escaping:
function submitWithEscape ()
{
    //escapeChars(document.getElementsByClassName("descriptionTextArea")[0]);
}

// Display Description Text w/ line breaks
function displayWithLineBreaks()
{
    if (document.getElementsByClassName("descriptionText").length != 0)
    {
        // For the Description Text:
        var temp = document.getElementsByClassName("descriptionText")[0].innerHTML;
        var temp1;
        document.getElementsByClassName("descriptionText")[0].innerHTML = ""; // Clear the current paragraph
        while (temp.indexOf("\n") != -1)
        {
            temp1 = document.createElement("P"); // Create a new paragraph element
            if (temp.indexOf("\n") != 0)
                temp1.innerHTML = temp.slice(0, temp.indexOf("\n")); // Place a whole line into the paragraph
            else
                temp1.innerHTML = "&nbsp;";
            temp1.style.margin = "0";
            document.getElementsByClassName("descriptionText")[0].appendChild(temp1); // Put the paragraph into the page for display
            temp = temp.slice(temp.indexOf("\n")+1); // Cut the string to continue to search for additional line breaks.
        }
        temp1 = document.createElement("P"); // Create a new paragraph element
        temp1.innerHTML = temp // Place the last line into the paragraph
        temp1.style.margin = "0";
        document.getElementsByClassName("descriptionText")[0].appendChild(temp1); // Put the paragraph into the page for display
    }
}
