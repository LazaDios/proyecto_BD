Create table if not exists customer(
    cedula varchar(11) not null primary key,
    name varchar(60) not null,
    whatsapp varchar(15) not null,
    email varchar(40) not null
); 

Create table if not exists orders(

    id serial not null  auto_increment primary key,

    cedula_cliente varchar(11) not null,
    quantity int(100) not null,
    payment_method varchar(100) not null,
    remarks varchar(600) not null, 
    city varchar(600) not null,
    municipality varchar(200) not null,
    

    total decimal(11,2) not null,
    payment_scrennshot varchar(400),
    delivery_amount decimal(11,2) not null,

    status varchar(55) not null,
    datetime varchar(100) not null,

    CONSTRAINT fk_pedido_cliente FOREIGN KEY(cedula_cliente) REFERENCES customer(cedula)
)