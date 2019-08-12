/* JavaScript file for: 'portIndex.html'
    version 1.0
    08.11.2019
    Description: Creation of File
- Front End Team
*/

// Function changing the color, title, backgorund image and text of the 'Save Post' button when pressed:
function saveOrUnsavePost ()
{
    var savePostButton = document.getElementsByClassName("savePost")[0];

    // If the post is still unsaved, save it.
    if (savePostButton.value == "Save Post")
    {
         savePostButton.style.backgroundColor = "#7B2240";
         savePostButton.style.backgroundImage = "url('static/img/grayFolder.png')";
         savePostButton.value = "Post Saved";
         savePostButton.title = "Post Saved";
    }
    // If the post is saved, unsave it.
    else 
    {
         savePostButton.style.backgroundColor = "#757575";
         savePostButton.style.backgroundImage = "url('static/img/maroonFolder.png')";
         savePostButton.value = "Save Post";
         savePostButton.title = "Save Post";
    }
    document.getElementsByClassName("savePostForm")[0].submit(); // Now submit this information
}

// Function changing the color of the 'upvotes' of posts when pressed to blue:
function forUpvote (object)
{
    // Extraction of specific post's or comment's class name:
    var specificClass = object.className.substr(10),
          upvoteButton, 
          downvoteButton, 
          numOfVotes;

    if (object.className.indexOf("upvoteBtnComment") == -1) // If the post was upvoted:
    {
              upvoteButton = document.getElementsByClassName("upvoteBtn " + specificClass)[0];
              downvoteButton = document.getElementsByClassName("downvoteBtn " + specificClass)[0];
              numOfVotes = document.getElementsByClassName("numOfVotes " + specificClass)[0];
    }
    else // If some comment was upvoted:
    {
              specificClass = specificClass.substr(9); // Retrieve the comment number
              upvoteButton = document.getElementsByClassName("upvoteBtn" + specificClass)[0];
              downvoteButton = document.getElementsByClassName("downvoteBtn" + specificClass)[0];
              numOfVotes = document.getElementsByClassName("numOfVotes" + specificClass)[0];
    }

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
    var specificClass = object.className.substr(12),
          upvoteButton, 
          downvoteButton, 
          numOfVotes;

    if (object.className.indexOf("downvoteBtnComment") == -1) // If the post was downvoted:
    {
              upvoteButton = document.getElementsByClassName("upvoteBtn " + specificClass)[0];
              downvoteButton = document.getElementsByClassName("downvoteBtn " + specificClass)[0];
              numOfVotes = document.getElementsByClassName("numOfVotes " + specificClass)[0];
    }
    else // If some comment was downvoted:
    {
              specificClass = specificClass.substr(11); // Retrieve the comment number
              upvoteButton = document.getElementsByClassName("upvoteBtn" + specificClass)[0];
              downvoteButton = document.getElementsByClassName("downvoteBtn" + specificClass)[0];
              numOfVotes = document.getElementsByClassName("numOfVotes" + specificClass)[0];
    }

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

// Unveal the Comment Area for a First Level Comment When Hitting 'Reply'
function unvealArea (comment)
{
    var theTextAreaDiv = document.getElementsByClassName("for" + comment)[0];
    if (theTextAreaDiv.style.display == "none")
    	theTextAreaDiv.style.display = "inherit";
    else
                 theTextAreaDiv.style.display = "none";
}

// Submit a comment to comment if ENTER was pressed and if the comment is nonempty:
function submitComment (comment)
{
    if ((event.which == 13 || event.keyCode == 13) 
                 && document.getElementsByClassName("commentToCommentText" + comment)[0].value.trim().length != 0)
        document.getElementsByClassName("writeCommentToComment" + comment)[0].submit();
}

// Enable the "submit comment" button if the comment to the post is nonempty, and disable it otherwise:
function enableDisableSubmission(theTextArea)
{
    if (theTextArea.value.trim().length != 0)
    {
         document.getElementsByClassName("CommentToPostBtn")[0].disabled = false;
         document.getElementsByClassName("CommentToPostBtn")[0].value = "✔   Submit Comment";
    }
    else
    {
         document.getElementsByClassName("CommentToPostBtn")[0].true = false;
         document.getElementsByClassName("CommentToPostBtn")[0].value = "✖   Submit Comment";
    }
}
