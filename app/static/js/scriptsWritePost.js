/* JavaScript file for 'writePost.html'
version 1.0
    08.08.2019
    Description: Creation
- Front End Team
*/

// A function writing the name of the uploaded file in the place of the "Add Image" button:
function changeVal ()
{
       if (document.getElementsByClassName("imageUpload")[0].value != '')
       	document.getElementsByClassName("imageLabel")[0].innerHTML = document.getElementsByClassName("imageUpload")[0].value;
       else
                 document.getElementsByClassName("imageLabel")[0].innerHTML = "Add Image";
}

// Make Received URLs no longer than 300 chars:
function URLLength ()
{
     if (document.getElementsByClassName("addimage")[0].value.length > 0)
     {
          document.getElementsByClassName("addimage")[0].required = true;
          if (document.getElementsByClassName("addimage")[0].value.length > 300)
               document.getElementsByClassName("addimage")[0].setCustomValidity("URL must be no longer than 300 chars!");
          else
               document.getElementsByClassName("addimage")[0].setCustomValidity("");
     }
     else
          document.getElementsByClassName("addimage")[0].required = false;
}

// Ensure the Post Title is at most 100 chars
function validateTitle ()
{
    if (document.getElementsByClassName("postTitle")[0].value.length > 100)
        document.getElementsByClassName("postTitle")[0].setCustomValidity("Title must be of at most 100 chars!");
    else
        document.getElementsByClassName("postTitle")[0].setCustomValidity("");
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
    // Create "new line" breaks in actual post text:
    document.getElementsByClassName("textOfPost")[0].value = document.getElementsByClassName("textOfPost")[0].value.replace(/(\r\n|\n)/g,"<br/>");
    escapeChars(document.getElementsByClassName("postTitle")[0]);
    escapeChars(document.getElementsByClassName("textOfPost")[0]);
}
