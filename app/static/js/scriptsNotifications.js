// A function that shortens the length of the post title and comment content if they are longer than 50 chars:
function cutIt ()
{
    for (i = 0; i < document.getElementsByClassName("nameOfPost").length; i++)
    {
         if (document.getElementsByClassName("nameOfPostOrComment")[i].innerHTML.length > 50)
                document.getElementsByClassName("nameOfPostOrComment")[i].innerHTML 
                             = document.getElementsByClassName("nameOfPostOrComment")[i].innerHTML.substr(0, 49) + "...";
         if (document.getElementsByClassName("theNoteContent")[i].innerHTML.length > 50)
                document.getElementsByClassName("theNoteContent")[i].innerHTML 
                             = document.getElementsByClassName("theNoteContent")[i].innerHTML.substr(0, 49) + "...";
    }
}