-- auto-generated definitions

-- clientes
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

-- productos
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

-- ventas
create table ventas
(
    id         integer not null
        constraint ventas_pk
            primary key autoincrement,
    id_cliente integer not null
        references clientes
            on delete cascade,
    fechahora  text default datetime('now', 'localtime') not null
);

create index ventas_id_cliente_index
    on ventas (id_cliente);

create unique index ventas_id_uindex
    on ventas (id);

-- contenido ventas
create table ventas_contenido
(
    id            integer not null
        constraint ventas_contenido_pk
            primary key autoincrement,
    id_venta      integer not null
        references ventas
            on delete cascade,
    id_producto   integer not null
        references productos
            on delete cascade,
    cantidad      integer not null,
    precio_unidad integer
);

create index ventas_contenido_id_producto_index
    on ventas_contenido (id_producto);

create unique index ventas_contenido_id_uindex
    on ventas_contenido (id);

create index ventas_contenido_id_venta_index
    on ventas_contenido (id_venta);

