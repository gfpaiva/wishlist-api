-- public.users definition

-- Drop table

-- DROP TABLE public.users;

CREATE TABLE public.users (
	id uuid NOT NULL DEFAULT uuid_generate_v4(),
	"name" varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	CONSTRAINT users_pkey PRIMARY KEY (id),
	CONSTRAINT users_un UNIQUE (email)
);

-- Permissions

ALTER TABLE public.users OWNER TO wishlist;
GRANT ALL ON TABLE public.users TO wishlist;


-- public.wishlists definition

-- Drop table

-- DROP TABLE public.wishlists;

CREATE TABLE public.wishlists (
	id uuid NOT NULL DEFAULT uuid_generate_v4(),
	title varchar(255) NOT NULL,
	description varchar(255) NOT NULL,
	user_id uuid NOT NULL,
	CONSTRAINT wishlists_pkey PRIMARY KEY (id),
	CONSTRAINT wishlists_fk FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Permissions

ALTER TABLE public.wishlists OWNER TO wishlist;
GRANT ALL ON TABLE public.wishlists TO wishlist;


-- public.wishlists_products definition

-- Drop table

-- DROP TABLE public.wishlists_products;

CREATE TABLE public.wishlists_products (
	id uuid NOT NULL DEFAULT uuid_generate_v4(),
	wishlist_id uuid NOT NULL,
	product_id uuid NOT NULL,
	CONSTRAINT wishlists_products_pkey PRIMARY KEY (id),
	CONSTRAINT wishlists_products_fk FOREIGN KEY (wishlist_id) REFERENCES wishlists(id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Permissions

ALTER TABLE public.wishlists_products OWNER TO wishlist;
GRANT ALL ON TABLE public.wishlists_products TO wishlist;