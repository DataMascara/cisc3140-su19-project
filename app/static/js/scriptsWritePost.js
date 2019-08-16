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
        else if (x.value[i] == "\n")
        {
            x.value[i] = "\\\n";
            i++;
        }
        else if (x.value[i] == "\f")
        {
            x.value[i] = "\\\f";
            i++;
        }
        else if (x.value[i] == "\r")
        {
            x.value[i] = "\\\r";
            i++;
        }
        else if (x.value[i] == "\v")
        {
            x.value[i] = "\\\v";
            i++;
        }
        else if (x.value[i] == "\t")
        {
            x.value[i] = "\\\t";
            i++;
        }
        else if (x.value[i] == "\0")
        {
            x.value[i] = "\\\0";
            i++;
        }
        else if (x.value[i] == "\'")
        {
            x.value[i] = "\\\'";
            i++;
        }
    //x.value = x.value.replace(/\\/g,'\\\\').replace(/\n/g,'\\\n').replace(/\f/g,'\\\f').replace(/\r/g,'\\\r').replace(/\t/g,'\\\t').replace(/\v/g,'\\\v').replace(/\0/g,'\\\0').replace(/\'/g,'\\\'').replace(/\"/g,'\"');
    }    
}
