
CREATE TABLE `users` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(30) NOT NULL,
    `first` VARCHAR(30) DEFAULT NULL,
    `last` VARCHAR(30) DEFAULT NULL,
    `email` VARCHAR(128) NOT NULL,
    `password` VARCHAR(128) NOT NULL,
    `description` VARCHAR(1000) NULL,
    `isActive` BOOLEAN NOT NULL DEFAULT '1',
    `avatarUrl` TEXT DEFAULT NULL,
    `dateModified` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `dateCreated` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `username` (`username`),
    UNIQUE KEY `email` (`email`)
);

CREATE TABLE `ports` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `isActive` BOOLEAN NOT NULL DEFAULT 1,
    `name` VARCHAR(30) NOT NULL,
    `description` VARCHAR(1000) NULL,
    `dateModified` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `dateCreated` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `name` (`name`)
);

CREATE TABLE `posts` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(100) NOT NULL,
    `text` TEXT NOT NULL,
    `imageUrl` TEXT NULL,
    `isDeleted` BOOLEAN NOT NULL DEFAULT 0,
    `portId` INTEGER NOT NULL,
    `userId` INTEGER NOT NULL,
    `dateModified` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `dateCreated` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `fkIdx_28` (`id`),
    CONSTRAINT `FK_28` FOREIGN KEY (`userId`)
        REFERENCES `users` (`id`),
    KEY `fkIdx_34` (`portId`),
    CONSTRAINT `FK_34` FOREIGN KEY (`portId`)
        REFERENCES `ports` (`id`),
    UNIQUE KEY `title` (`title`)
);

CREATE TABLE `comments` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `postId` INTEGER NOT NULL,
    `text` TEXT NOT NULL,
    `parentId` INTEGER NULL,
    `isDeleted` BOOLEAN NOT NULL DEFAULT 0,
    `userId` INTEGER NOT NULL,
    `dateModified` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `dateCreated` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `fkIdx_51` (`userId`),
    CONSTRAINT `FK_51` FOREIGN KEY (`userId`)
        REFERENCES `users` (`id`),
    KEY `fkIdx_54` (`postId`),
    CONSTRAINT `FK_54` FOREIGN KEY (`postId`)
        REFERENCES `posts` (`id`)
);

CREATE TABLE `subscriptions` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `isActive` BOOLEAN NOT NULL DEFAULT 1,
    `portId` INTEGER NOT NULL,
    `userId` INTEGER NOT NULL,
    `dateModified` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `dateCreated` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `fkIdx_14` (`userId`),
    CONSTRAINT `FK_14` FOREIGN KEY (`userId`)
        REFERENCES `users` (`id`),
    KEY `fkIdx_17` (`portId`),
    CONSTRAINT `FK_17` FOREIGN KEY (`portId`)
        REFERENCES `ports` (`id`),
    UNIQUE KEY `uniquePortandUser` (`portId` , `userId`)
);

CREATE TABLE `ads` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `adUrl` TEXT NOT NULL,
    `image` TEXT NOT NULL,
    `text` VARCHAR(1000) NOT NULL,
    `isActive` BOOLEAN NOT NULL DEFAULT 0,
    `dateModified` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `dateCreated` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);

CREATE TABLE `votes` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `userId` INTEGER NOT NULL,
    `postId` INTEGER NULL,
    `commentId` INTEGER NULL,
    `isSaved` BOOLEAN NOT NULL DEFAULT 0,
    `vote` INTEGER NOT NULL DEFAULT 0,
    `dateModified` DATETIME DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    `dateCreated` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `fkIdx_101` (`postId`),
    CONSTRAINT `FK_101` FOREIGN KEY (`postId`)
        REFERENCES `posts` (`id`),
    KEY `fkIdx_107` (`commentId`),
    CONSTRAINT `FK_107` FOREIGN KEY (`commentId`)
        REFERENCES `comments` (`id`),
    KEY `fkIdx_98` (`userId`),
    CONSTRAINT `FK_98` FOREIGN KEY (`userId`)
        REFERENCES `users` (`id`),
    UNIQUE KEY `uniqueUserperPost` (`userId` , `postId`),
    UNIQUE KEY `uniqueUserperComment` (`userId` , `commentId`)
);


#trigger to add a subscription to the main port when a user is added
DELIMITER //

CREATE TRIGGER subscriptionOnUserInsert
AFTER INSERT
   ON users FOR EACH ROW

BEGIN
	#adds an automatic subscription to 'main' port for every new user
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
	#adds an automatic upvote for every user's own added post
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
#adds an automatic upvote for every user's own added comment
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


CREATE VIEW posts_vw AS
    SELECT 
        pr.name AS portName,
        p.id AS postId,
        p.title AS postTitle,
        p.text AS postText,
        p.imageUrl AS image,
        u.username AS author,
        CAST(SUM(vote) AS CHAR (10)) AS votes,
        (SELECT 
                CAST(COUNT(id) AS CHAR (10))
            FROM
                comments c
            WHERE
                c.postId = p.id) AS numComments,
        p.dateCreated
    FROM
        posts p
            LEFT JOIN
        users u ON p.userid = u.id
            LEFT JOIN
        votes v ON v.postid = p.id
            LEFT JOIN
        ports pr ON pr.id = p.portid
    WHERE
        p.isDeleted = 0
    GROUP BY p.id
    ORDER BY p.id;

CREATE VIEW comments_vw AS
    SELECT 
        p.postId,
        c.id AS commentId,
        c.text AS commentText,
        u.username AS author,
        CAST(SUM(vote) AS CHAR (10)) AS votes,
        parentId
    FROM
        comments c
            LEFT JOIN
        posts_vw p ON c.postid = p.postId
            LEFT JOIN
        votes v ON v.commentid = c.id
            LEFT JOIN
        users u ON u.id = c.userid
    WHERE
        c.isDeleted = 0
    GROUP BY c.id;CREATE VIEW subscriptions_vw AS
    SELECT 
        username, p.id AS portId, p.name AS portName
    FROM
        subscriptions s
            JOIN
        users u ON u.id = s.userid
            JOIN
        ports p ON p.id = s.portid
    WHERE
        s.isActive = 1;

CREATE VIEW votes_vw AS
    SELECT DISTINCT
        p.id AS postId,
        p.title AS Title,
        p.imageUrl AS Image,
        p.text AS Text,
        u.username AS author,
        uv.username AS voteUsername,
        vote,
        isSaved,
        'Post' AS type
    FROM
        posts p
            LEFT JOIN
        users u ON p.userid = u.id
            LEFT JOIN
        votes v ON v.postid = p.id
            JOIN
        users uv ON uv.id = v.userid
    WHERE
        isDeleted = 0 
    UNION SELECT DISTINCT
        c.id AS commentId,
        '' AS Title,
        '' AS Image,
        c.text AS Text,
        u.username AS author,
        uv.username AS voteUsername,
        vote,
        isSaved,
        'Comment' AS type
    FROM
        comments c
            LEFT JOIN
        users u ON u.id = c.userid
            LEFT JOIN
        votes v ON v.commentid = c.id
            JOIN
        users uv ON uv.id = v.userid
    WHERE
        c.isDeleted = 0;

CREATE VIEW users_vw AS
    SELECT 
        u.id AS userId,
        password,
        username,
        first,
        last,
        email,
        description,
        avatarUrl,
        CAST(SUM(vote) AS CHAR (10)) AS votes
    FROM
        users u
            LEFT JOIN
        votes_vw v ON u.username = v.author
    WHERE
        u.isActive = 1
    GROUP BY u.id; #group by userID to get sum of votes per user's posts and comments



DELIMITER $$
#this function adds a post and returns the new post's ID. 
CREATE FUNCTION add_post(title varchar(360), text varchar(1000), port_name varchar(30), author varchar(30), image text) RETURNS INTEGER
    DETERMINISTIC
BEGIN
    DECLARE newId INTEGER;
	#insert the post
    INSERT INTO posts (title, text, portId, userid, imageUrl) VALUES 
    (title, text, (SELECT id FROM ports WHERE name = port_name), (SELECT id FROM users WHERE username = author), image);
	#set the variable to be the new post's ID
 	SET newId =  LAST_INSERT_ID();
	#return the new ID
 RETURN (newId);
END








