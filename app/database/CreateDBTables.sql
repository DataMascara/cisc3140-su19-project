
#create all tables in the database by executing this file

#users table saves user information
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,   #auto generated
  `username` varchar(30) NOT NULL,            
  `first` varchar(30) DEFAULT NULL,           
  `last` varchar(30) DEFAULT NULL,            
  `email` varchar(128) NOT NULL,              
  `password` varchar(128) NOT NULL,
  `description` varchar(1000) NULL,
  `isActive` boolean NOT NULL DEFAULT '1',    #check for deleted account
  `avatarUrl` text DEFAULT NULL,      #hold image url for avatar or profile pic
  `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
  `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`), #username must be unique
  UNIQUE KEY `email` (`email`)	#email must be unique
);

#ports table saves port/forum information
CREATE TABLE `ports`(
 `id`       integer NOT NULL auto_increment,#auto generated
 `isActive`     boolean NOT NULL default 1,     #is port currently active
 `name`     varchar(30) NOT NULL ,          #unique name for port
 `description` varchar(1000) NULL,
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
`dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  
PRIMARY KEY (`id`),
UNIQUE KEY `name` (`name`)	#port name must be unique
);

#posts table saves post information
CREATE TABLE `posts`(
 `id`       integer NOT NULL auto_increment,      #auto generated
 `title`	varchar(100) NOT NULL,				
 `text`     text NOT NULL ,
 `isDeleted`    boolean NOT NULL DEFAULT 0,           #is post deleted or not
 `portId`       integer NOT NULL ,                    #FK referencing the post
 `userId`       integer NOT NULL ,                    #FK referencing the author from users table
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  
PRIMARY KEY (`id`),
KEY `fkIdx_28` (`id`),
CONSTRAINT `FK_28` FOREIGN KEY `fkIdx_28` (`userId`) REFERENCES `users` (`id`),
KEY `fkIdx_34` (`portId`),
CONSTRAINT `FK_34` FOREIGN KEY `fkIdx_34` (`portId`) REFERENCES `ports` (`id`),
UNIQUE KEY `title` (`title`)
);

#comments table saves comment information
CREATE TABLE `comments`(
 `id`    integer NOT NULL auto_increment,        #auto generated
 `postId`       integer NOT NULL ,                      #FK referencing the post
 `text`  text NOT NULL ,
 `parentId`     integer NULL ,                          #FK referencing the parent comment
 `isDeleted`    boolean NOT NULL default 0,             #is comment deleted or not
 `userId`       integer NOT NULL ,                      #FK referencing the author from users table
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  

PRIMARY KEY (`id`),
KEY `fkIdx_51` (`userId`),
CONSTRAINT `FK_51` FOREIGN KEY `fkIdx_51` (`userId`) REFERENCES `users` (`id`),
KEY `fkIdx_54` (`postId`),
CONSTRAINT `FK_54` FOREIGN KEY `fkIdx_54` (`postId`) REFERENCES `posts` (`id`)
);

#subscriptions table saves subscription information
CREATE TABLE `subscriptions`(
 `id`       integer NOT NULL auto_increment,     #auto generated
 `isActive`     boolean NOT NULL default 1,          #current subscription or deleted
 `portId`       integer NOT NULL ,                   #FK referencing the port 
 `userId`       integer NOT NULL ,                   #FK referencing the user
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  
PRIMARY KEY (`id`),
KEY `fkIdx_14` (`userId`),
CONSTRAINT `FK_14` FOREIGN KEY `fkIdx_14` (`userId`) REFERENCES `users` (`id`),
KEY `fkIdx_17` (`portId`),
CONSTRAINT `FK_17` FOREIGN KEY `fkIdx_17` (`portId`) REFERENCES `ports` (`id`),
UNIQUE KEY `uniquePortandUser` (`portId`, `userId`) #doesn't allow duplicate subscriptions
);

#ads table saves ad information
CREATE TABLE `ads`(
 `id`     integer NOT NULL auto_increment,    #auto generated
 `adUrl`    text NOT NULL ,
 `image` text NOT NULL ,
 `text`   varchar(1000) NOT NULL ,
 `isActive` boolean not null default 0,          #is ad currently active on site or not
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  
PRIMARY KEY (`id`)
);

#table to record users' saved posts and upvoted or downvoted posts and comments
CREATE TABLE `votes`
(
 `id`      integer NOT NULL AUTO_INCREMENT,    #auto generated
 `userId`      integer NOT NULL , 					#FK referencing the user
 `postId`      integer NULL ,						#FK referencing the post (optional)
 `commentId`   integer NULL ,						#FK referencing the comment (optional) -->either the postid or commentid must be filled
 `isSaved`     boolean NOT NULL DEFAULT 0,			#is comment or post saved
 `vote`  	   integer NOT NULL DEFAULT 0,			#1 for upvote, -1 for downvote, 0 for no vote
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
 
PRIMARY KEY (`id`),
KEY `fkIdx_101` (`postId`),
CONSTRAINT `FK_101` FOREIGN KEY `fkIdx_101` (`postId`) REFERENCES `posts` (`id`),
KEY `fkIdx_107` (`commentId`),
CONSTRAINT `FK_107` FOREIGN KEY `fkIdx_107` (`commentId`) REFERENCES `comments` (`id`),
KEY `fkIdx_98` (`userId`),
CONSTRAINT `FK_98` FOREIGN KEY `fkIdx_98` (`userId`) REFERENCES `users` (`id`),
UNIQUE KEY `uniqueUserperPost` (`userId`, `postId`), #only one vote per post per user
UNIQUE KEY `uniqueUserperComment` (`userId`, `commentId`) #only one vote per comment per user
);


#trigger to add a subscription to the main port when a user is added
DELIMITER //

CREATE TRIGGER subscriptionOnUserInsert
AFTER INSERT
   ON users FOR EACH ROW

BEGIN

   INSERT INTO subscriptions
   ( userId,
     portId)
   VALUES
   ( NEW.id,
     (select id from ports where name = 'main'));

END; //

DELIMITER ;

#trigger to auto-upvote a user's post when posted
DELIMITER //

CREATE TRIGGER upvoteOnPostInsert
AFTER INSERT
   ON posts FOR EACH ROW

BEGIN

   INSERT INTO votes
   ( userId,
     postId,
     vote)
   VALUES
   ( NEW.userId,
	 NEW.id,
    1);

END; //

DELIMITER ;


#trigger to auto-upvote a user's comment when posted
DELIMITER //

CREATE TRIGGER upvoteOnCommentInsert
AFTER INSERT
   ON comments FOR EACH ROW

BEGIN

   INSERT INTO votes
   ( userId,
     commentId,
     vote)
   VALUES
   ( NEW.userId,
	NEW.id,
    1);

END; //

DELIMITER ;





create view posts_vw as
    #votes are being cast as char(10) because the integer sums were not showing up through the python functions for some reason
select pr.name as portName, p.id as postId, p.text as postText, u.username as author, 
cast(sum(vote) as char(10)) as votes, (select cast(count(id) as char(10)) from comments c where c.postId = p.id) as numComments, p.dateCreated
from posts p
left join users u on p.userid = u.id
left join votes v on v.postid = p.id
left join ports pr on pr.id = p.portid
where p.isDeleted = 0
group by p.id
Order by p.id;
select * from comments;

create view comments_vw as
    #votes are being cast as char(10) because the integer sums were not showing up through the python functions for some reason
select p.postId, c.id as commentId, c.text as commentText, u.username as author, cast(sum(vote) as char(10)) as votes, parentId
from comments c 
left join posts_vw p on c.postid = p.postId
left join votes v on v.commentid = c.id
left join users u on u.id = c.userid
where c.isDeleted = 0
group by c.id;


create view subscriptions_vw as
select username, p.id as portId, p.name as portName
from subscriptions s 
join users u on u.id = s.userid
join ports p on p.id = s.portid
where s.isActive = 1;

create view votes_vw as
  #votes are being cast as char(10) because the integer sums were not showing up through the python functions for some reason
select distinct p.id as postId, p.text as Text, u.username as author, uv.username as voteUsername, vote, isSaved, 'Post' as type
from posts p
left join users u on p.userid = u.id
left join votes v on v.postid = p.id
join users uv on uv.id = v.userid
where isDeleted = 0
union
select distinct c.id as commentId, c.text as Text, u.username as author, uv.username as voteUsername, vote, isSaved, 'Comment' as type
from comments c
left join users u on u.id = c.userid
left join votes v on v.commentid = c.id
join users uv on uv.id = v.userid
where c.isDeleted = 0;

create view users_vw as
select u.id as userId, password, username, first, last, email, description, avatarUrl, cast(sum(vote) as char(10)) as votes
from users u
left join votes_vw v on u.username = v.author
where u.isActive = 1
group by u.id;












