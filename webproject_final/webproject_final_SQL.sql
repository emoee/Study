create database RestaurantsDB character set utf8;
CREATE TABLE store (
  s_id int NOT NULL,
  s_name varchar(20) NOT NULL,
  s_address varchar(20) NOT NULL,
  s_img1_fname varchar(30) DEFAULT NULL,
  s_description varchar(100) DEFAULT NULL,
  PRIMARY KEY (s_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE cust (
  c_id int NOT NULL,
  c_name varchar(10) NOT NULL,
  c_phone varchar(15) NOT NULL,
  c_email varchar(40) NOT NULL,
  PRIMARY KEY (c_id),
  UNIQUE KEY c_email (c_email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE menu (
  m_id int NOT NULL,
  m_s_id int NOT NULL,
  m_name varchar(10) NOT NULL,
  m_price int NOT NULL,
  m_img1_fname varchar(30) DEFAULT NULL,
  m_content varchar(200) DEFAULT NULL,
  PRIMARY KEY (m_id),
  KEY m_s_id (m_s_id),
  CONSTRAINT menu_ibfk_1 FOREIGN KEY (m_s_id) REFERENCES store (s_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE r_order (
  o_id int NOT NULL,
  o_s_id int DEFAULT NULL,
  o_date varchar(15) NOT NULL,
  o_c_id int DEFAULT NULL,
  PRIMARY KEY (o_id),
  KEY o_s_id (o_s_id),
  KEY o_c_id (o_c_id),
  CONSTRAINT r_order_ibfk_3 FOREIGN KEY (o_s_id) REFERENCES store (s_id) ON DELETE CASCADE,
  CONSTRAINT r_order_ibfk_4 FOREIGN KEY (o_c_id) REFERENCES cust (c_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE order_menu (
  om_id int NOT NULL,
  om_o_id int NOT NULL,
  PRIMARY KEY (om_o_id),
  KEY o_id_idx (om_o_id),
  KEY om_id (om_id),
  CONSTRAINT order_menu_ibfk_1 FOREIGN KEY (om_o_id) REFERENCES r_order (o_id) ON DELETE CASCADE,
  CONSTRAINT order_menu_ibfk_2 FOREIGN KEY (om_id) REFERENCES menu (m_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;