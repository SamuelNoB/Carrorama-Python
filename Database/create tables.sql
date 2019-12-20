CREATE DATABASE carrorama;

CREATE TABLE IF NOT EXISTS `carrorama`.`Veiculo` (
  `idVeiculo` INT NOT NULL AUTO_INCREMENT,
  `modelo` VARCHAR(40) NULL,
  `marca` VARCHAR(45) NULL,
  `cor` VARCHAR(20) NULL,
  `placa` VARCHAR(8) NULL,
  `renavam` VARCHAR(13) NULL,
  `motor` FLOAT NULL,
  `ano` YEAR NULL,
  PRIMARY KEY (`idVeiculo`),
  UNIQUE INDEX `renavam_UNIQUE` (`renavam` ASC) VISIBLE,
  UNIQUE INDEX `placa_UNIQUE` (`placa` ASC) VISIBLE)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `carrorama`.`Combustiveis` (
  `combustivel` INT NOT NULL,
  `Veiculo_idVeiculo` INT NOT NULL,
  PRIMARY KEY (`combustivel`, `Veiculo_idVeiculo`),
  INDEX `fk_Combustiveis_Veiculo_idx` (`Veiculo_idVeiculo` ASC) VISIBLE,
  CONSTRAINT `fk_Combustiveis_Veiculo`
    FOREIGN KEY (`Veiculo_idVeiculo`)
    REFERENCES `carrorama`.`Veiculo` (`idVeiculo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `carrorama`.`Despesa` (
  `idDespesa` INT NOT NULL AUTO_INCREMENT,
  `categoria` INT NULL,
  `valor` FLOAT NULL,
  `DATA` DATE NULL,
  `Veiculo_idVeiculo` INT NOT NULL,
  PRIMARY KEY (`idDespesa`, `Veiculo_idVeiculo`),
  INDEX `fk_despesa_Veiculo1_idx` (`Veiculo_idVeiculo` ASC) VISIBLE,
  CONSTRAINT `fk_despesa_Veiculo1`
    FOREIGN KEY (`Veiculo_idVeiculo`)
    REFERENCES `carrorama`.`Veiculo` (`idVeiculo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `carrorama`.`Abastecimento` (
  `idAbastecimento` INT NOT NULL AUTO_INCREMENT,
  `combustiveis` INT UNSIGNED NULL,
  `quilometragem_inicial` FLOAT NULL,
  `valor_do_litro` FLOAT NULL,
  `tanque_cheio` TINYINT NULL,
  `despesa_iddespesa` INT NOT NULL,
  PRIMARY KEY (`idAbastecimento`, `despesa_iddespesa`),
  INDEX `fk_Abastecimento_despesa1_idx` (`despesa_iddespesa` ASC) VISIBLE,
  CONSTRAINT `fk_Abastecimento_despesa1`
    FOREIGN KEY (`despesa_iddespesa`)
    REFERENCES `carrorama`.`Despesa` (`idDespesa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `carrorama`.`manutencao` (
  `idmanutencao` INT NOT NULL AUTO_INCREMENT,
  `quilometragem` FLOAT NULL,
  `despesa_iddespesa` INT NOT NULL,
  PRIMARY KEY (`idmanutencao`, `despesa_iddespesa`),
  INDEX `fk_manutencao_despesa1_idx` (`despesa_iddespesa` ASC) VISIBLE,
  CONSTRAINT `fk_manutencao_despesa1`
    FOREIGN KEY (`despesa_iddespesa`)
    REFERENCES `carrorama`.`Despesa` (`idDespesa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;