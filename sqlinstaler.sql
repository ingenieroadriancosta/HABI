use habi_db;
-- creacion de tabla userlikes
create table if not exists userlikes(
id int primary key auto_increment,
id_user int not null,
id_property int not null,
likeopt char not null,
date_of_like datetime DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_user) REFERENCES auth_user(id),
FOREIGN KEY (id_property) REFERENCES property(id),
UNIQUE KEY itemuser (`id_user`,`id_property`)
);
