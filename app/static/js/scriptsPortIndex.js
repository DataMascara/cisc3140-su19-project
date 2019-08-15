/* JavaScript file
    version 1.1.1
    08.13.2019
    Description: `subscribePortIndex` was modified to fix the button coordination bug. Bug fixed!
    
    version 1.1
    08.13.2019
    Description: Pressing 'subscribe' on the port index will change the color of the corresponding button in 'Trending Ports'. Bug fixed!
    
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
    
   // Now check if this port is also in the 'trending ports' section, and change the color of the button accordingly:
   for (i = 0; i < document.getElementsByClassName("trendingName").length; i+=2)
   {
        if (document.getElementsByClassName("trendingName")[i].innerHTML == document.getElementsByClassName("portName" + id)[0].innerHTML)
        {
                // Note that the index below is 'i/2'. The reason is that another element has the classname "trendingName", which is
                // why we need to skip over the odd numbers to get to the corresponding button!
                document.getElementsByClassName("subscribe")[i/2].style.backgroundColor = subscribeButton.style.backgroundColor;
                document.getElementsByClassName("subscribe")[i/2].value = subscribeButton.value;
                document.getElementsByClassName("subscribe")[i/2].title = subscribeButton.title;
        }
   }
    
   document.getElementsByClassName("subscriptionForm" + id)[0].submit(); // Now submit this information
}
