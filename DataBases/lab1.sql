
CREATE TABLE users (
    id bigint NOT NULL PRIMARY KEY,
    firstname varchar(50) NOT NULL,
    lastname varchar(50) NOT NULL,
    isadmin BOOLEAN DEFAULT 'FALSE'
);

CREATE TABLE tasks (
    id bigint NOT NULL PRIMARY KEY,
    name varchar(50) NOT NULL,
    user_id BIGINT NOT NULL,

    CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES users (id)
);

INSERT INTO users (id, firstname, lastname)
VALUES (1, 'David','Dik' );

INSERT INTO tasks (id, name, user_id)
VALUES (1, 'sleep',  1);
