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
   document.getElementById("trendingForm").submit(); // Now submit this information
}