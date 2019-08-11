/* JavaScript file
    version 1.0
    08.11.2019
    Description: Creation of File
- Front End Team
*/

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
   document.getElementsByClassName("subscriptionForm" + id)[0].submit(); // Now submit this information
}