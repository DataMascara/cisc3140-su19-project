#create all tables in the database by executing this file

#users table saves user information
CREATE TABLE `users` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,   #auto generated
  `username` varchar(30) NOT NULL,            
  `first` varchar(30) DEFAULT NULL,           
  `last` varchar(30) DEFAULT NULL,            
  `email` varchar(128) NOT NULL,              
  `password` varchar(128) NOT NULL,
  `isActive` boolean NOT NULL DEFAULT '1',    #check for deleted account
  `avatarUrl` varchar(128) DEFAULT NULL,      #hold image url for avatar or profile pic
  `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
  `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  PRIMARY KEY (`userid`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=246815 DEFAULT CHARSET=utf8;

#ports table saves port/forum information
CREATE TABLE `ports`(
 `portid`       integer NOT NULL auto_increment,#auto generated
 `isActive`     boolean NOT NULL default 1,     #is port currently active
 `portname`     varchar(30) NOT NULL ,          #unique name for port
 `userid`       integer  NULL,                  #(optional) user that created the port
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
`dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  
PRIMARY KEY (`portid`),
KEY `fkIdx_20` (`userid`),
CONSTRAINT `FK_20` FOREIGN KEY `fkIdx_20` (`userid`) REFERENCES `users` (`userid`),
UNIQUE KEY `portname` (`portname`)
);

#posts table saves post information
CREATE TABLE `posts`(
 `postid`       integer NOT NULL auto_increment,      #auto generated
 `posttext`     text NOT NULL ,
 `isDeleted`    boolean NOT NULL DEFAULT 0,           #is post deleted or not
 `portid`       integer NOT NULL ,                    #FK referencing the post
 `userid`       integer NOT NULL ,                    #FK referencing the author from users table
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  
PRIMARY KEY (`postid`),
KEY `fkIdx_28` (`userid`),
CONSTRAINT `FK_28` FOREIGN KEY `fkIdx_28` (`userid`) REFERENCES `users` (`userid`),
KEY `fkIdx_34` (`portid`),
CONSTRAINT `FK_34` FOREIGN KEY `fkIdx_34` (`portid`) REFERENCES `ports` (`portid`)
);

#comments table saves comment information
CREATE TABLE `comments`(
 `commentid`    integer NOT NULL auto_increment,        #auto generated
 `postid`       integer NOT NULL ,                      #FK referencing the post
 `commenttext`  text NOT NULL ,
 `parentid`     integer NOT NULL ,                      #FK referencing the parent comment or post
 `isDeleted`    boolean NOT NULL default 0,             #is comment deleted or not
 `userid`       integer NOT NULL ,                      #FK referencing the author from users table
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  

PRIMARY KEY (`commentid`),
KEY `fkIdx_51` (`userid`),
CONSTRAINT `FK_51` FOREIGN KEY `fkIdx_51` (`userid`) REFERENCES `users` (`userid`),
KEY `fkIdx_54` (`postid`),
CONSTRAINT `FK_54` FOREIGN KEY `fkIdx_54` (`postid`) REFERENCES `posts` (`postid`)
);

#subscriptions table saves subscription information
CREATE TABLE `subscriptions`(
 `lineid`       integer NOT NULL auto_increment,     #auto generated
 `isActive`     boolean NOT NULL default 1,          #current subscription or deleted
 `portid`       integer NOT NULL ,                   #FK referencing the port 
 `userid`       integer NOT NULL ,                   #FK referencing the user
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  
PRIMARY KEY (`lineid`),
KEY `fkIdx_14` (`userid`),
CONSTRAINT `FK_14` FOREIGN KEY `fkIdx_14` (`userid`) REFERENCES `users` (`userid`),
KEY `fkIdx_17` (`portid`),
CONSTRAINT `FK_17` FOREIGN KEY `fkIdx_17` (`portid`) REFERENCES `ports` (`portid`)
);

#ads table saves ad information
CREATE TABLE `ads`(
 `adid`     integer NOT NULL auto_increment,    #auto generated
 `adurl`    varchar(128) NOT NULL ,
 `imageurl` varchar(128) NOT NULL ,
 `adtext`   varchar(700) NOT NULL ,
 `isActive` boolean not null default 0,          #is ad currently active on site or not
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion
  
PRIMARY KEY (`adid`)
);

#table to record users' saved posts and upvoted or downvoted posts and comments
CREATE TABLE `votes`
(
 `lineid`      integer NOT NULL AUTO_INCREMENT,    #auto generated
 `userid`      integer NOT NULL , 					#FK referencing the user
 `postid`      integer NULL ,						#FK referencing the post (optional)
 `commentid`   integer NULL ,						#FK referencing the comment (optional) -->either the postid or commentid must be filled
 `isSaved`     boolean NOT NULL DEFAULT 0,			#is comment or post saved
 `vote`  	   tinyint NOT NULL DEFAULT 0,			#1 for upvote, -1 for downvote, 0 for no vote
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP, #auto updated
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,        #auto generated on row insertion

PRIMARY KEY (`lineid`),
KEY `fkIdx_101` (`postid`),
CONSTRAINT `FK_101` FOREIGN KEY `fkIdx_101` (`postid`) REFERENCES `posts` (`postid`),
KEY `fkIdx_107` (`commentid`),
CONSTRAINT `FK_107` FOREIGN KEY `fkIdx_107` (`commentid`) REFERENCES `comments` (`commentid`),
KEY `fkIdx_98` (`userid`),
CONSTRAINT `FK_98` FOREIGN KEY `fkIdx_98` (`userid`) REFERENCES `users` (`userid`)
);

































