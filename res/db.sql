-- auto-generated definition
create table clientes
(
    id        integer     not null
        constraint clientes_pk
            primary key autoincrement,
    dni       varchar2(9) not null,
    nombre    varchar2(12),
    apellido  varchar2(12),
    telefono  int,
    direccion varchar2(20)
);

create unique index clientes_dni_uindex
    on clientes (dni);

create unique index clientes_id_uindex
    on clientes (id);


-- auto-generated definition
create table productos
(
    id          integer not null
        constraint productos_pk
            primary key autoincrement,
    nombre      varchar2(12),
    descripcion varchar2(24),
    precio      integer,
    stock       integer
);

create unique index productos_id_uindex
    on productos (id);

