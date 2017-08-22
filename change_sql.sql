/* 2017-08-14 add three tables */
CREATE TABLE `SEQ_SA_INFO`.`billing_info` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `project_id` INT NULL,
  `project_number` VARCHAR(45) NULL,
  `expense` INT NULL,
  `billing_number` VARCHAR(45) NULL,
  `time` DATETIME NULL,
  `comment` VARCHAR(100) NULL,
  PRIMARY KEY (`id`))
  ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `SEQ_SA_INFO`.`receipt_info` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `project_id` INT NULL,
    `project_number` VARCHAR(45) NULL,
    `expense` INT NULL,
    `time` DATETIME NULL,
    `comment` VARCHAR(100) NULL,
    PRIMARY KEY (`id`))
    ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `SEQ_SA_INFO`.`cost_info` (
      `id` INT NOT NULL AUTO_INCREMENT,
      `project_id` INT NULL,
      `project_number` VARCHAR(45) NULL,
      `expense` INT NULL,
      `sample_number` VARCHAR(45) NULL,
      `unit_cost` VARCHAR(45) NULL,
      `time` DATETIME NULL,
      `comment` VARCHAR(100) NULL,
      PRIMARY KEY (`id`))
      ENGINE=InnoDB DEFAULT CHARSET=utf8;
/* 2017-08-17 alter tables:
- send_sample
- quality_check
- build_lib
- upmachine
- downmachine
add upload_time save and om_id three fields
*/
ALTER TABLE `SEQ_SA_INFO`.`send_sample`
CHANGE COLUMN `time` `create_time` DATETIME NULL DEFAULT NULL ,
ADD COLUMN `upload_time` VARCHAR(45) NULL AFTER `comment`,
ADD COLUMN `status` VARCHAR(1) NULL AFTER `upload_time`,
ADD COLUMN `om_id` VARCHAR(100) NULL AFTER `species`;

ALTER TABLE `SEQ_SA_INFO`.`quality_check`
CHANGE COLUMN `time` `create_time` DATETIME NULL DEFAULT NULL ,
ADD COLUMN `upload_time`  VARCHAR(45)  NULL AFTER `comment`,
ADD COLUMN `status` VARCHAR(1) NULL AFTER `upload_time`,
ADD COLUMN `om_id` VARCHAR(100) NULL AFTER `sample_name`;

ALTER TABLE `SEQ_SA_INFO`.`build_lib`
CHANGE COLUMN `time` `create_time` DATETIME NULL DEFAULT NULL ,
ADD COLUMN `upload_time`  VARCHAR(45)  NULL AFTER `comment`,
ADD COLUMN `status` VARCHAR(1) NULL AFTER `upload_time`,
ADD COLUMN `om_id` VARCHAR(100) NULL AFTER `sample_name`;

ALTER TABLE `SEQ_SA_INFO`.`upmachine`
CHANGE COLUMN `time` `create_time` DATETIME NULL DEFAULT NULL ,
ADD COLUMN `upload_time`  VARCHAR(45)  NULL AFTER `comment`,
ADD COLUMN `status` VARCHAR(1) NULL AFTER `upload_time`,
ADD COLUMN `om_id` VARCHAR(100) NULL AFTER `sample_name`;

ALTER TABLE `SEQ_SA_INFO`.`downmachine`
CHANGE COLUMN `time` `create_time` DATETIME NULL DEFAULT NULL ,
ADD COLUMN `upload_time`  VARCHAR(45)  NULL AFTER `comment`,
ADD COLUMN `status` VARCHAR(1) NULL AFTER `upload_time`,
ADD COLUMN `om_id` VARCHAR(100) NULL AFTER `sample_name`;
/* 2017-08-21
*/
ALTER TABLE `SEQ_SA_INFO`.`quality_check`
DROP INDEX `sample_id_UNIQUE` ;
ALTER TABLE `SEQ_SA_INFO`.`build_lib`
DROP INDEX `sample_id_UNIQUE` ;
ALTER TABLE `SEQ_SA_INFO`.`upmachine`
DROP INDEX `sample_id_UNIQUE` ;
ALTER TABLE `SEQ_SA_INFO`.`downmachine`
DROP INDEX `sample_id_UNIQUE` ;
