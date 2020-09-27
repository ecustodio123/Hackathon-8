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
