Text taken from cisc3140-su19-project/docs/notes-to-other/to-backend/ pdf file.
Code blocks include the dbmodule function you will need with an example of it being used.

1. (Displays Posts of some Port) Given a Port id: (1) query the database with this id to receive an JSON array of Posts ids written via the port, and (2) query the database again with those Posts ids to receive a JSON array of the following info per each Post:
(1) name of Post (2) content (3) image (4) day (5) month (6) year (7) hour (8) minute (9) name of the User who wrote it (10) image of the User who wrote it, (11) number of votes, and (12) number of Comments. 
>`#function dbmodule.posts_db.all_posts_by(column_name, data_value)`
>
> `dbmodule.posts_db.all_posts_by('portId', 1)`
>
> `dbmodule.posts_db.all_posts_by('portName', 'main')`

The table in the database for the Post object has the id of the User who wrote the post, and his or her name and image in (9) and (10)above can be retrieved by querying the database in the table of User objects. 
>`#function dbmodule.users_db.find_users(column_name, data_value)`
>
>`dbmodule.users_db.find_users('username','chalshaff12')`
2. Do the same as above, except that you obtain a JSON array that is sorted based on the
highest number of votes.

3. (Display Posts Relevant to User) Given a User id, (1) query the database to obtain
the ids of all the Ports to which the User is subscribed, and 
>`#function dbmodule.subscriptions_db.all_subscriptions_by(column_name, data_value)`
>`dbmodule.subscriptions_db.all_subscriptions_by('username','chalshaff12')`

(2) per each Port, repeat
the steps in 1 such that the array of all the Posts from all these Ports will be sorted
based on date and time.
4. Do the same as above, but make sure the Posts are sorted based on the highest number
of votes.
5. (Display all Info about a Post) Given a Post id, query the database for: (1) name of
Post (2) content (3) image (4) day (5) month (6) year (7) hour (8) minute (9) name of
the User who wrote it (10) image of the User who wrote it, (11) number of votes, and
(12) number of Comments. This very JSON bulb that you receive should also contain
inner (nested) JSON bulbs that will represent information about Comments to this Post.
The JSON bulb for a Comment should include: (1) content (text of Comment), (2) day (3)
month (4) year (5) hour (6) minute, (7) number of votes to the Comment, (8) username
of User who wrote the Comment, (9) 
>`#dbmodule.comments_db.all_comments_by(column_name, data_value)`
>
>`dbmodule.comments_db.all_comments_by('postId','1')`

the image of the User, and (10) inner JSON bulbs
with Comments to the Comment.
>`#for nested comments:`
>
>`dbmodule.comments_db.all_comments_by('parentId','4')` 
>
>`#parentId is the comment ID of the parent comment`

As you probably notice while reading this paragraph,
there is a theoretical option for innitely many nested JSON bulbs, which is practically
a disaster. Hence, I will ask the Product team if they will allow us to limit the nesting
of Comments to some level. For example, Facebook allows only two levels of Comments
(so we have the original Post, Comments to the Post, and Comments to those Comments,
and that's it.) If they will allow this, there will be at maximum two nesting levels in
the outer JSON code.
1
Front-End team Possible Tasks you would Master July 25, 2019
6. (User Registration) Request information from a form on our template that will contain:
(1) User's rst name (2) User's last name (3) username (= login name) (4) email
address (5) password, and (6) image. Send this info into the database to create a new
User instance.
>`#function dbmodule.users_db.add_user(email, password, username, first, last, description, avatarurl):`
>
>`dbmodule.users_db.add_user('doctor_bad_w@gmail.com', 'hashedpasswordblue', 'badwolfisnotme', 'Doctor', 'Who', 'Im a cool doctor who flies through space and time','www.image.jpg')`

7. (User Login) Request information from a form on our template that will contain: (1)
username, and (2) password. Authenticate this info with the database, and if it exists
and accurate, redirect
>`dbmodule.users_db.find_user('username','chalshaff12')`
>
>`#this will return username,password, email etc so you can verify the password from the returned fields`



Add post:
>`#function dbmodule.post_db.add_post(title, text, port_id, author_id)`
>
>`dbmodule.post_db.add_post('This is a new post','Here is the text of the post, it might be longer',3,2)`
