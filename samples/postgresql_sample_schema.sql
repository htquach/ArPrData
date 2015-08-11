--
-- PostgreSQL sample database to run with the sample policies.yml
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: ArPrDataDemo; Type: SCHEMA; Schema: -; Owner: htquach
--

CREATE SCHEMA "ArPrDataDemo";


ALTER SCHEMA "ArPrDataDemo" OWNER TO htquach;

--
-- Name: SCHEMA "ArPrDataDemo"; Type: COMMENT; Schema: -; Owner: htquach
--

COMMENT ON SCHEMA "ArPrDataDemo" IS 'A demo database to use with ArPrData application published on GitHub.  ArPrData is a project from CS561 Summer 2015.';


SET search_path = "ArPrDataDemo", pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Table1; Type: TABLE; Schema: ArPrDataDemo; Owner: htquach; Tablespace:
--

CREATE TABLE "Table1" (
    id integer NOT NULL,
    created_date timestamp without time zone DEFAULT now(),
    modified_date timestamp without time zone DEFAULT now()
);


ALTER TABLE "ArPrDataDemo"."Table1" OWNER TO htquach;

--
-- Name: TABLE "Table1"; Type: COMMENT; Schema: ArPrDataDemo; Owner: htquach
--

COMMENT ON TABLE "Table1" IS 'Table1 with dummy data';


--
-- Name: Table1Archive; Type: TABLE; Schema: ArPrDataDemo; Owner: htquach; Tablespace:
--

CREATE TABLE "Table1Archive" (
    id integer NOT NULL,
    created_date timestamp without time zone,
    modified_date timestamp without time zone
);


ALTER TABLE "ArPrDataDemo"."Table1Archive" OWNER TO htquach;

--
-- Name: Table1_id_seq; Type: SEQUENCE; Schema: ArPrDataDemo; Owner: htquach
--

CREATE SEQUENCE "Table1_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "ArPrDataDemo"."Table1_id_seq" OWNER TO htquach;

--
-- Name: Table1_id_seq; Type: SEQUENCE OWNED BY; Schema: ArPrDataDemo; Owner: htquach
--

ALTER SEQUENCE "Table1_id_seq" OWNED BY "Table1".id;


--
-- Name: Table2; Type: TABLE; Schema: ArPrDataDemo; Owner: htquach; Tablespace:
--

CREATE TABLE "Table2" (
    id integer NOT NULL,
    created_date timestamp without time zone DEFAULT now() NOT NULL,
    int_val integer,
    text_val text,
    real_val real
);


ALTER TABLE "ArPrDataDemo"."Table2" OWNER TO htquach;

--
-- Name: Table2Archive; Type: TABLE; Schema: ArPrDataDemo; Owner: htquach; Tablespace:
--

CREATE TABLE "Table2Archive" (
    id integer NOT NULL,
    created_date timestamp without time zone NOT NULL,
    int_val integer,
    text_val text,
    real_val real
);


ALTER TABLE "ArPrDataDemo"."Table2Archive" OWNER TO htquach;

--
-- Name: Table2_id_seq; Type: SEQUENCE; Schema: ArPrDataDemo; Owner: htquach
--

CREATE SEQUENCE "Table2_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "ArPrDataDemo"."Table2_id_seq" OWNER TO htquach;

--
-- Name: Table2_id_seq; Type: SEQUENCE OWNED BY; Schema: ArPrDataDemo; Owner: htquach
--

ALTER SEQUENCE "Table2_id_seq" OWNED BY "Table2".id;


--
-- Name: id; Type: DEFAULT; Schema: ArPrDataDemo; Owner: htquach
--

ALTER TABLE ONLY "Table1" ALTER COLUMN id SET DEFAULT nextval('"Table1_id_seq"'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: ArPrDataDemo; Owner: htquach
--

ALTER TABLE ONLY "Table2" ALTER COLUMN id SET DEFAULT nextval('"Table2_id_seq"'::regclass);


--
-- Name: Table1_pkey; Type: CONSTRAINT; Schema: ArPrDataDemo; Owner: htquach; Tablespace:
--

ALTER TABLE ONLY "Table1"
    ADD CONSTRAINT "Table1_pkey" PRIMARY KEY (id);


--
-- Name: Table2_pkey; Type: CONSTRAINT; Schema: ArPrDataDemo; Owner: htquach; Tablespace:
--

ALTER TABLE ONLY "Table2"
    ADD CONSTRAINT "Table2_pkey" PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--
