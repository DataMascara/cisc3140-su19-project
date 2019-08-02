/* JavaScript file
version 1.0
    08.02.2019
    Description: These are functions operating on the 2 base templates 'baseLoggedIn.html' and 'baseLoggedOut.html'
    This file should not prospectively change.
    Back-End Team: try to connect to the templates without using this file, or using Ajax.
    See README.md for explanation of how to send arguments via 'render_template' and obtain info via 'request.form'
    Thank you so much!
- Front End Team
*/

// A function that toggles the opening and closing of the menu bar (previously was in jQuery, but changed to vanilla JS)
function openCloseSidebar ()
{
       if (!document.getElementsByClassName ("sidebar")[0].classList.contains("active"))
            document.getElementsByClassName ("sidebar")[0].classList.add("active");
       else
            document.getElementsByClassName ("sidebar")[0].classList.remove("active");
}

// Submit the search if ENTER was pressed:
function submitSearch ()
{
    if (event.which == 13 || event.keyCode == 13)
        document.getElementsByClassName("searchform")[0].submit();
}

// Change the color of the subscription button and what is written on it if it is pressed. Then, submit the form:
function subscribe(x)
{
   var temp = x.id.substr(x.id.length - 1); // Fetch the last char. of the id of the calling button. This is its serial number given as a string.
   if (x.value ==  'Subscribe')
   {
       x.style.backgroundColor = 'rgb(123, 34, 64)'; // It means the user is subscribed to the particular port. Color the calling button maroon, and
       x.value = 'Joined'; // Change the text on the button to 'joined'.
   }
   else // Otherwise, if the user clicked again (to unsubscribe):
   {
       x.style.backgroundColor = 'rgb(117, 117, 117)'; // Turn the color back to gray,
       x.value = 'Subscribe'; // Change the text on the button to 'Subscribe'.
   }
   document.getElementsByClassName("trendingForm")[0].submit(); // Now submit this information
}

// If the user is not logged in, the menu bar will open, and the input fields and the buttons will glow blue.
function ifLoggedOutGlowSignIn ()
{
      if (document.getElementsByClassName ("sidebar")[0].classList.contains("active"))
           openCloseSidebar ();
      document.getElementsByClassName("button1")[0].style.backgroundColor = 'DeepSkyBlue';
      document.getElementsByClassName("button2")[0].style.backgroundColor = 'DeepSkyBlue';
      document.getElementsByClassName("text")[0].style.backgroundColor = 'DeepSkyBlue';
      document.getElementsByClassName("text")[1].style.backgroundColor = 'DeepSkyBlue';
      setTimeout( function()
      {
                  document.getElementsByClassName("button1")[0].style.backgroundColor = '#757575';
                  document.getElementsByClassName("button2")[0].style.backgroundColor = '#757575';
                  document.getElementsByClassName("text")[0].style.backgroundColor = 'white';
                  document.getElementsByClassName("text")[1].style.backgroundColor = 'white';
      },1000);
}

// Display the current year inside the 'copyright' division
function displayYear()
{
     document.getElementsByClassName("year")[0].innerHTML = (new Date()).getFullYear();
}