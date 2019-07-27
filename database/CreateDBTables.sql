#create all tables in the database by executing this file

#users table saves user information
CREATE TABLE `users` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first` varchar(30) DEFAULT NULL,
  `last` varchar(30) DEFAULT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `isActive` boolean NOT NULL DEFAULT '1',
  `avatarUrl` varchar(128) DEFAULT NULL,
  `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`userid`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=246815 DEFAULT CHARSET=utf8;

#ports table saves port/forum information
CREATE TABLE `ports`(
 `portid`       integer NOT NULL auto_increment,
 `isActive`     boolean NOT NULL default 1,
 `portname`     varchar(30) NOT NULL ,
 `userid`       integer  NULL,
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,

PRIMARY KEY (`portid`),
KEY `fkIdx_20` (`userid`),
CONSTRAINT `FK_20` FOREIGN KEY `fkIdx_20` (`userid`) REFERENCES `users` (`userid`)
);

#posts table saves post information
CREATE TABLE `posts`(
 `postid`       integer NOT NULL auto_increment,
 `posttext`     text NOT NULL ,
 `upvotes`      integer NULL ,
 `downvotes`    integer NULL ,
 `isDeleted`    boolean NOT NULL DEFAULT 0,
 `portid`       integer NOT NULL ,
 `userid`       integer NOT NULL ,
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,

PRIMARY KEY (`postid`),
KEY `fkIdx_28` (`userid`),
CONSTRAINT `FK_28` FOREIGN KEY `fkIdx_28` (`userid`) REFERENCES `users` (`userid`),
KEY `fkIdx_34` (`portid`),
CONSTRAINT `FK_34` FOREIGN KEY `fkIdx_34` (`portid`) REFERENCES `ports` (`portid`)
);

#comments table saves comment information
CREATE TABLE `comments`(
 `commentid`    integer NOT NULL auto_increment,
 `postid`       integer NOT NULL ,
 `commenttext`  text NOT NULL ,
 `parentid`     integer NOT NULL ,
 `upvotes`      integer NULL ,
 `downvotes`    integer NULL ,
 `isDeleted`    boolean NOT NULL default 0,
 `userid`       integer NOT NULL ,
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,


PRIMARY KEY (`commentid`),
KEY `fkIdx_51` (`userid`),
CONSTRAINT `FK_51` FOREIGN KEY `fkIdx_51` (`userid`) REFERENCES `users` (`userid`),
KEY `fkIdx_54` (`postid`),
CONSTRAINT `FK_54` FOREIGN KEY `fkIdx_54` (`postid`) REFERENCES `posts` (`postid`)
);

#subscriptions table saves subscription information
CREATE TABLE `subscriptions`(
 `lineid`       integer NOT NULL auto_increment,
 `isActive`     boolean NOT NULL default 1,
 `portid`       integer NOT NULL ,
 `userid`       integer NOT NULL ,
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,

PRIMARY KEY (`lineid`),
KEY `fkIdx_14` (`userid`),
CONSTRAINT `FK_14` FOREIGN KEY `fkIdx_14` (`userid`) REFERENCES `users` (`userid`),
KEY `fkIdx_17` (`portid`),
CONSTRAINT `FK_17` FOREIGN KEY `fkIdx_17` (`portid`) REFERENCES `ports` (`portid`)
);

#ads table saves ad information
CREATE TABLE `ads`(
 `adid`     integer NOT NULL auto_increment,
 `adurl`    varchar(128) NOT NULL ,
 `imageurl` varchar(128) NOT NULL ,
 `adtext`   varchar(700) NOT NULL ,
 `isActive` boolean not null default 0,
 `dateModified` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
 `dateCreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
 
PRIMARY KEY (`adid`)
);





































