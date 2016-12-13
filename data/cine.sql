create database Cine;
use Cine;
create table detalle_renta( 
    id_renta int not null auto_increment primary key,
    pelicula varchar(50) not null,
    formato varchar(10) not null,
    tiempo varchar(2) not null,
    total varchar(4) not null

);

select * from detalle_renta;
