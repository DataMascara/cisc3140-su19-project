/* JavaScript file for: 'portIndex.html'
    version 1.1
    08.13.2019
    Description: correction of folder location of static images
    
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
         savePostButton.style.backgroundImage = "url('../static/img/grayFolder.png')";
         savePostButton.value = "Post Saved";
         savePostButton.title = "Post Saved";
    }
    // If the post is saved, unsave it.
    else 
    {
         savePostButton.style.backgroundColor = "#757575";
         savePostButton.style.backgroundImage = "url('../static/img/maroonFolder.png')";
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

// Enable the "submit comment" button if the comment to the post is nonempty, and disable it otherwise:
function enableDisableSubmission(theTextArea)
{
    if (theTextArea.className.length == 17)
    {
        if (theTextArea.value.trim().length != 0)
        {
             document.getElementsByClassName("CommentToPostBtn")[0].disabled = false;
             document.getElementsByClassName("CommentToPostBtn")[0].value = "✔   Submit Comment";
        }
        else
        {
             document.getElementsByClassName("CommentToPostBtn")[0].disabled = true;
             document.getElementsByClassName("CommentToPostBtn")[0].value = "✖   Submit Comment";
        }
    }
    else
    {
         // Extract the 'id' of the comment;
         var id = theTextArea.className.substr(38);
         // Check if area is non empty:
         if (theTextArea.value.trim().length != 0)
        {
             document.getElementsByClassName("buttonComment" + id)[0].disabled = false;
             document.getElementsByClassName("buttonComment" + id)[0].value = "✔   Submit Comment";
        }
        else
        {
             document.getElementsByClassName("buttonComment" + id)[0].disabled = true;
             document.getElementsByClassName("buttonComment" + id)[0].value = "✖   Submit Comment";
        }
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

// Submit the Comment to Post form w/ escaping:
function submitWithEscapeCommentToPost ()
{
    escapeChars(document.getElementsByClassName("commentToPostText")[0]);
}


// Submit the Comment to Post form w/ escaping:
function submitWithEscapeCommentToComment (obj)
{
    var id = obj.className.substr(21);
    escapeChars(document.getElementsByClassName("commentToCommentText" + id)[0]);
}

// Display Post Text w/ line breaks
function displayWithLineBreaks()
{
    // For the Post Text:
    var temp = document.getElementsByClassName("postDescription")[0].innerHTML;
    var temp1;
    document.getElementsByClassName("postDescription")[0].innerHTML = ""; // Clear the current paragraph
    while (temp.indexOf("\n") != -1)
    {
        temp1 = document.createElement("P"); // Create a new paragraph element
        if (temp.indexOf("\n") != 0)
            temp1.innerHTML = temp.slice(0, temp.indexOf("\n")); // Place a whole line into the paragraph
        else
            temp1.innerHTML = "&nbsp;";
        temp1.style.margin = "0";
        document.getElementsByClassName("postDescription")[0].appendChild(temp1); // Put the paragraph into the page for display
        temp = temp.slice(temp.indexOf("\n")+1); // Cut the string to continue to search for additional line breaks.
    }
    temp1 = document.createElement("P"); // Create a new paragraph element
    temp1.innerHTML = temp // Place the last line into the paragraph
    temp1.style.margin = "0";
    document.getElementsByClassName("postDescription")[0].appendChild(temp1); // Put the paragraph into the page for display
    
    // For all the Comments (whatever level) on the page:
    for (i = 0; i < document.getElementsByClassName("commentText").length; i++)
    {
            temp = document.getElementsByClassName("commentText")[i].innerHTML;
            document.getElementsByClassName("commentText")[i].innerHTML = ""; // Clear the current paragraph
            while (temp.indexOf("\n") != -1)
            {
                temp1 = document.createElement("P"); // Create a new paragraph element
                if (temp.indexOf("\n") != 0)
                    temp1.innerHTML = temp.slice(0, temp.indexOf("\n")); // Place a whole line into the paragraph
                else
                    temp1.innerHTML = "&nbsp;";
                temp1.style.margin = "0";
                document.getElementsByClassName("commentText")[i].appendChild(temp1); // Put the paragraph into the page for display
                temp = temp.slice(temp.indexOf("\n")+1); // Cut the string to continue to search for additional line breaks.
            }
            temp1 = document.createElement("P"); // Create a new paragraph element
            temp1.innerHTML = temp // Place the last line into the paragraph
            temp1.style.margin = "0";
            document.getElementsByClassName("commentText")[i].appendChild(temp1); // Put the paragraph into the page for display
    }
}
