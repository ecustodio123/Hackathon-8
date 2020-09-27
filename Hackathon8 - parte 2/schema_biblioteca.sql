-- Database: biblioteca

-- DROP DATABASE biblioteca;

CREATE DATABASE biblioteca
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- TABLAS
-- informacion_libro

-- Table: public.informacion_libro

-- DROP TABLE public.informacion_libro;

CREATE TABLE public.informacion_libro
(
    id_libro SERIAL, --('informacion_libro_id_libro_seq'::regclass),
    isbn character varying(150) COLLATE pg_catalog."default",
    nombre_del_libro character varying(150) COLLATE pg_catalog."default",
    autor character varying(150) COLLATE pg_catalog."default",
    editorial character varying(150) COLLATE pg_catalog."default",
    estado_libro character varying(150) COLLATE pg_catalog."default",
    nombre_del_lector character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT informacion_libro_pkey PRIMARY KEY (id_libro)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.informacion_libro
    OWNER to postgres;

-- informacion_lector
-- Table: public.informacion_lector

-- DROP TABLE public.informacion_lector;

CREATE TABLE public.informacion_lector
(
    id_lector SERIAL, --('informacion_lector_id_lector_seq'::regclass),
    nombre_del_lector character varying(150) COLLATE pg_catalog."default",
    dni character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT informacion_lector_pkey PRIMARY KEY (id_lector)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.informacion_lector
    OWNER to postgres;

-- roles
-- Table: public.roles

-- DROP TABLE public.roles;

CREATE TABLE public.roles
(
    id_rol SERIAL, --('roles_id_rol_seq'::regclass),
    nombre character varying(150) COLLATE pg_catalog."default",
    contrasena character varying(150) COLLATE pg_catalog."default",
    cargo character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT roles_pkey PRIMARY KEY (id_rol)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.roles
    OWNER to postgres;

-- POR FAVOR COLOCAR LA SENTENCIA SIGUIENTE
-- Esto va generar un usuario administrado, cuyos datos seran:
-- usuario: admin
-- contraseña: password
-- cargo: admin
-- Esto para poder utilizar bien el programa, y se puede registrar más usuarios con cargo admin o lector.

INSERT INTO roles (nombre, contrasena, cargo) VALUES
('admin', 'password', 'admin')
