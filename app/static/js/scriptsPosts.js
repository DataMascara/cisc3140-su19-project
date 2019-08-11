// Function changing the color of the 'upvotes' of posts when pressed to blue:
function forUpvote (object)
{
    // Extraction of specific post's class name:
    var specificClass = object.className.substr(10);

    var upvoteButton = document.getElementsByClassName("upvoteBtn " + specificClass)[0],
          downvoteButton = document.getElementsByClassName("downvoteBtn " + specificClass)[0],
          numOfVotes = document.getElementsByClassName("numOfVotes " + specificClass)[0];

    if (downvoteButton.style.color == "red")
    {
         downvoteButton.style.color = "black";
         numOfVotes.style.color = "black";
         numOfVotes.innerText = parseInt(numOfVotes.innerText) + 1;
    }

    if (upvoteButton.style.color == "rgb(77, 208, 191)")
    {
         upvoteButton.style.color = "black";
         numOfVotes.style.color = "black";
         numOfVotes.innerText = parseInt(numOfVotes.innerText) - 1;
    }
    else
    {
         upvoteButton.style.color = "rgb(77, 208, 191)";
         numOfVotes.style.color = "rgb(77, 208, 191)";
         numOfVotes.innerText = parseInt(numOfVotes.innerText) + 1;
    }
}

// Function changing the color of the 'downvotes' of posts when pressed to red:
function forDownvote (object)
{
    // Extraction of specific post's class name:
    var specificClass = object.className.substr(12);

    var upvoteButton = document.getElementsByClassName("upvoteBtn " + specificClass)[0],
          downvoteButton = document.getElementsByClassName("downvoteBtn " + specificClass)[0],
          numOfVotes = document.getElementsByClassName("numOfVotes " + specificClass)[0];

    if (upvoteButton.style.color == "rgb(77, 208, 191)")
    {
         upvoteButton.style.color = "black";
         numOfVotes.style.color = "black";
         numOfVotes.innerText = parseInt(numOfVotes.innerText) - 1;
    }

    if (downvoteButton.style.color == "red")
    {
         downvoteButton.style.color = "black";
         numOfVotes.style.color = "black";
         numOfVotes.innerText = parseInt(numOfVotes.innerText) + 1;
    }
    else
    {
         downvoteButton.style.color = "red";
         numOfVotes.style.color = "red";
         numOfVotes.innerText = parseInt(numOfVotes.innerText) - 1;
    }
}

// A function that shortens the length of the post title and description if they are longer than 36 chars:
function cutIt ()
{
    for (i = 0; i < document.getElementsByClassName("nameOfPost").length; i++)
    {
         if (document.getElementsByClassName("nameOfPost")[i].innerHTML.length > 36)
                document.getElementsByClassName("nameOfPost")[i].innerHTML 
                             = document.getElementsByClassName("nameOfPost")[i].innerHTML.substr(0, 35) + "...";
         if (document.getElementsByClassName("postDescription")[i] && document.getElementsByClassName("postDescription")[i].innerHTML.length > 36)
                document.getElementsByClassName("postDescription")[i].innerHTML 
                             = document.getElementsByClassName("postDescription")[i].innerHTML.substr(0, 35) + "...";
    }
}