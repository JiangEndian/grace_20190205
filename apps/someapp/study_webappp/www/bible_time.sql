drop database if exists bible;

create database bible;

use bible;

grant select, insert, update, delete on bible.* to 'editer'@'localhost' identified by 'editer';

create table bible_time (
    `id` varchar(50) not null,
    `aa_start` bigint not null,
    `aa_end` bigint not null,
    `name` varchar(50) not null,
    `last` bigint not null,
    `ad_start` bigint not null,
    `ad_end` bigint not null,
    `content` mediumtext not null,
    `other1` varchar(50),
    `other2` varchar(50),
    `other3` varchar(50),
    `created_at` real not null,
    key `idx_created_at` (`created_at`),
    primary key(`id`)
) engine=innodb default charset=utf8;
