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
