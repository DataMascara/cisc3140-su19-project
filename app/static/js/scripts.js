/* JavaScript file
version 1.0
    08.02.2019
    Description: These are functions operating on the 2 base templates 'baseLoggedIn.html' and 'baseLoggedOut.html'
    This file should not prospectively change.
    Back-End Team: try to connect to the templates without using this file, or using Ajax.
    See README.md for explanation of how to send arguments via 'render_template' and obtain info via 'request.form'
    Thank you so much!
- Front End Team


08.04.2019
Description:Example calling the API and responding to the HTML sign-in form submission
Front-End Team:Please see below example where you'd call this js function from a form (or anywhere) and use the api to ger a response, and then base the html and css off of this response. To do this I edited the login form, and added this validate as the onclick and passed in the form values. 
*/
async function validate(username, password) {
  //Would do other validation using API here
  const response = await fetch(`http://127.0.0.1:5000/test/${username}`);
  const jsonData = await response.json();
  //Log the API's response for debugging
  console.log(jsonData);
  try {
    let res = "";
    //If there is a user, here is where it would be from the api
    if (jsonData["users"]) {
      res = jsonData["users"][0]; // We grab the first user that comes back
    } else {
      //If the user doesnt exist, the json will have this key
      res = jsonData["error"];
    }
    //See what resulted
    console.log(res);
    //Return the result
    return res;
    //Catch any other error
  } catch (err) {
    console.error(err);
    //Log for debug and return the error
    return err;
  }
}

// A function that toggles the opening and closing of the menu bar (previously was in jQuery, but changed to vanilla JS)
function openCloseSidebar() {
  if (
    !document.getElementsByClassName("sidebar")[0].classList.contains("active")
  )
    document.getElementsByClassName("sidebar")[0].classList.add("active");
  else document.getElementsByClassName("sidebar")[0].classList.remove("active");
}

// Submit the search if ENTER was pressed:
function submitSearch() {
  if (event.which == 13 || event.keyCode == 13)
    document.getElementsByClassName("searchform")[0].submit();
}

// Change the color of the subscription button and what is written on it if it is pressed. Then, submit the form:
function subscribe(x) {
  var temp = x.id.substr(x.id.length - 1); // Fetch the last char. of the id of the calling button. This is its serial number given as a string.
  if (x.value == "Subscribe") {
    x.style.backgroundColor = "rgb(123, 34, 64)"; // It means the user is subscribed to the particular port. Color the calling button maroon, and
    x.value = "Joined"; // Change the text on the button to 'joined'.
  } // Otherwise, if the user clicked again (to unsubscribe):
  else {
    x.style.backgroundColor = "rgb(117, 117, 117)"; // Turn the color back to gray,
    x.value = "Subscribe"; // Change the text on the button to 'Subscribe'.
  }
  document.getElementsByClassName("trendingForm")[0].submit(); // Now submit this information
}

// If the user is not logged in, the menu bar will open, and the input fields and the buttons will glow blue.
function ifLoggedOutGlowSignIn() {
  if (
    document.getElementsByClassName("sidebar")[0].classList.contains("active")
  )
    openCloseSidebar();
  document.getElementsByClassName("button1")[0].style.backgroundColor =
    "DeepSkyBlue";
  document.getElementsByClassName("button2")[0].style.backgroundColor =
    "DeepSkyBlue";
  document.getElementsByClassName("text")[0].style.backgroundColor =
    "DeepSkyBlue";
  document.getElementsByClassName("text")[1].style.backgroundColor =
    "DeepSkyBlue";
  setTimeout(function() {
    document.getElementsByClassName("button1")[0].style.backgroundColor =
      "#757575";
    document.getElementsByClassName("button2")[0].style.backgroundColor =
      "#757575";
    document.getElementsByClassName("text")[0].style.backgroundColor = "white";
    document.getElementsByClassName("text")[1].style.backgroundColor = "white";
  }, 1000);
}

// Display the current year inside the 'copyright' division
function displayYear() {
  document.getElementsByClassName(
    "year"
  )[0].innerHTML = new Date().getFullYear();
}
