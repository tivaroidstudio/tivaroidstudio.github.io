#!/usr/bin/env python3
"""
Generates the static SEO pages of TivaroSQL Studio under /tivarosqlstudio/ plus sitemap.xml and robots.txt.
Run from the repository root:  python3 tools/build_sqlstudio.py
Edit the content below (PAGES, GUIDES, landing texts), never the generated HTML.
"""
import html, json, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://tivaroidstudio.github.io"
APP = "/tivarosql-studio/"
PLAY = "https://play.google.com/store/apps/details?id=tivaro.sql.studio"
TODAY = datetime.date.today().isoformat()
OUT = ROOT / "tivarosql-studio"


def play(campaign):
    # UTM tags show up in Play Console → Store listing acquisition (no analytics on the site itself).
    return f"{PLAY}&utm_source=tivaroid_site&utm_medium=website&utm_campaign={campaign}"


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------- engine pages (English, long-tail SEO)
# Every claim here must match the shipping app (see TivaroSQLStudio/src/lib/engines.ts and README).
PAGES = [
    {
        "slug": "postgresql-client-android",
        "name": "PostgreSQL",
        "title": "PostgreSQL Client for Android – Query Postgres from Your Phone",
        "desc": "Free PostgreSQL client for Android: SQL editor, table browser, row editing, SSL and SSH tunnel. Works with Neon, Supabase, Amazon RDS, Redshift, CockroachDB and TimescaleDB.",
        "h1": "PostgreSQL client for Android",
        "lead": "Connect to PostgreSQL straight from your phone, run queries with autocomplete, browse schemas and fix rows – without a laptop and without any server in the middle.",
        "shot": "3-results",
        "works": "Neon, Supabase, Amazon RDS / Aurora, Amazon Redshift, CockroachDB, TimescaleDB, YugabyteDB and any server that speaks the PostgreSQL wire protocol.",
        "steps": [
            "Tap <b>+ New</b> and choose <b>PostgreSQL</b> – or paste a <code>postgresql://user@host:5432/db</code> URL or a JDBC string and the form fills itself in.",
            "Pick the SSL mode (<code>disable</code>, <code>prefer</code>, <code>require</code> or <code>verify-full</code>). Cloud providers such as Neon and Supabase need <code>require</code>.",
            "Optionally tag the connection as <b>PROD</b> and switch on <b>read-only</b> – the session is then opened read-only by the server.",
            "Tap <b>Connect</b>. Schemas, tables and views appear in the navigator; open the SQL tab and start typing.",
        ],
        "features": [
            ("Schemas, tables, views", "Columns with types, primary keys, indexes and the full DDL of every table."),
            ("Real SQL editor", "Syntax highlighting, table and column suggestions above the keyboard, run the statement under the cursor."),
            ("Safe row editing", "Edit, insert or delete rows of tables with a primary key – each change is shown as SQL before it runs."),
            ("Transactions", "Switch off auto-commit and use Commit / Rollback buttons – one persistent session per connection."),
            ("EXPLAIN & ER diagram (Pro)", "Readable query plans with warnings about sequential scans and an interactive diagram of foreign keys."),
            ("SSH tunnel (Pro)", "Reach databases in a private network through a bastion host, with server key verification."),
        ],
        "faq": [
            ("Is there a free PostgreSQL client for Android?", "Yes. TivaroSQL Studio is free to download; running SQL, browsing and editing tables work in the free version. Pro adds unlimited connections and tabs, SSH tunnel, EXPLAIN and the ER diagram."),
            ("Can I connect to Supabase or Neon from my phone?", "Yes. Use the host, database, user and password from the provider's dashboard (or paste the connection string) and set SSL to require."),
            ("Does the app send my data to a server?", "No. The phone connects directly to your database. There is no account, no analytics and passwords are encrypted with Android Keystore."),
        ],
    },
    {
        "slug": "mysql-client-android",
        "name": "MySQL",
        "title": "MySQL & MariaDB Client for Android – SQL Editor on Your Phone",
        "desc": "Free MySQL and MariaDB client for Android. Run queries, browse tables, edit rows, export CSV. Works with PlanetScale, TiDB, Amazon RDS, SingleStore, StarRocks and Doris.",
        "h1": "MySQL & MariaDB client for Android",
        "lead": "A fast MySQL client in your pocket: write SQL, look at your tables and correct data on any MySQL or MariaDB server – from home, the train or an on-call night.",
        "shot": "2-editor",
        "works": "MySQL 5.7 / 8.x, MariaDB, PlanetScale, TiDB, Amazon RDS / Aurora MySQL, SingleStore, StarRocks, Apache Doris and other MySQL-compatible servers.",
        "steps": [
            "Tap <b>+ New</b> and choose <b>MySQL / MariaDB</b>, or paste a <code>mysql://</code> URL or <code>jdbc:mysql://</code> string.",
            "Enter host, port (3306 by default), database and user. Enable SSL for cloud services such as PlanetScale or TiDB Cloud.",
            "Tag the connection DEV, TEST or PROD – production connections ask for confirmation before every change.",
            "Connect, pick a table and tap <b>Data</b>, or open the SQL tab to run your own queries.",
        ],
        "features": [
            ("Browse tables", "Columns, indexes and DDL for every table and view."),
            ("Editor with suggestions", "Table and column names suggested above the keyboard, SQL formatter, undo / redo."),
            ("Edit rows safely", "Change values, add and delete rows with an SQL preview before saving."),
            ("Export", "CSV and JSON for free; Excel-friendly CSV, TSV, SQL INSERT and Markdown in Pro."),
            ("Charts", "Turn any result into a bar or line chart with one tap."),
            ("Import CSV / Excel (Pro)", "Load a spreadsheet into a table directly from your phone."),
        ],
        "faq": [
            ("Can I use it with MariaDB?", "Yes. MariaDB speaks the MySQL protocol and is fully supported."),
            ("Does it work with PlanetScale?", "Yes. Use the host, user and password generated in PlanetScale and keep SSL enabled."),
            ("Is it free?", "The app is free with core features. Pro is a one-time purchase or a monthly subscription."),
        ],
    },
    {
        "slug": "sql-server-client-android",
        "name": "SQL Server",
        "title": "SQL Server Client for Android – Connect to MSSQL & Azure SQL",
        "desc": "Microsoft SQL Server client for Android with a T-SQL editor, table browser and data editing. Connects to on-premises SQL Server and Azure SQL Database over TLS.",
        "h1": "SQL Server client for Android",
        "lead": "Query Microsoft SQL Server and Azure SQL from your phone: a native TDS driver, a T-SQL editor and a clean data grid – no remote desktop, no VPN app gymnastics.",
        "shot": "7-plan",
        "works": "Microsoft SQL Server (Standard, Enterprise, Express, Developer) and Azure SQL Database.",
        "steps": [
            "Tap <b>+ New</b> → <b>SQL Server</b>, or paste a <code>jdbc:sqlserver://host;databaseName=…</code> string.",
            "Enter host, port 1433, database, user and password. For Azure SQL keep encryption on.",
            "Use <b>read-only</b> mode for reporting accounts and tag production servers as PROD.",
            "Connect and run T-SQL; results appear in a sortable, filterable grid.",
        ],
        "features": [
            ("T-SQL editor", "Highlighting, suggestions, run the whole script or only the current statement."),
            ("Objects", "Schemas, tables and views with columns, indexes and DDL."),
            ("Row editing", "Edit tables that have a primary key, with an SQL preview."),
            ("Azure SQL", "Works with Azure SQL Database over TLS."),
            ("Desktop layout", "Connect the phone to a monitor (Samsung DeX) for a three-pane IDE."),
            ("Export", "CSV, JSON and – in Pro – Excel CSV, TSV, SQL INSERT and Markdown."),
        ],
        "faq": [
            ("Does it need a VPN or a gateway?", "No gateway. The phone connects directly to the server, so it must be reachable from your network – or use the SSH tunnel (Pro)."),
            ("Can I connect to Azure SQL Database?", "Yes, with SQL authentication over an encrypted connection."),
            ("Are my passwords safe?", "Passwords are encrypted with Android Keystore and never leave the device."),
        ],
    },
    {
        "slug": "oracle-client-android",
        "name": "Oracle",
        "title": "Oracle Database Client for Android – No Instant Client Needed",
        "desc": "Oracle Database client for Android with a built-in thin driver: run SQL and PL/SQL, browse schemas and tables. No Oracle Instant Client or JDBC required.",
        "h1": "Oracle Database client for Android",
        "lead": "Run SQL and PL/SQL against Oracle Database from your phone. The thin driver is built in – nothing to install, no Instant Client, no Java.",
        "shot": "2-editor",
        "works": "Oracle Database (including the free 23ai edition) and Oracle Autonomous Database, using a host, port and service name.",
        "steps": [
            "Tap <b>+ New</b> → <b>Oracle</b>.",
            "Enter host, port 1521 and the <b>service name</b> (for example <code>FREEPDB1</code>), then user and password.",
            "Tag the connection and choose auto-commit or manual transactions with Commit / Rollback.",
            "Connect – unquoted names are upper-cased the Oracle way, so <code>select * from employees</code> just works.",
        ],
        "features": [
            ("Built-in thin driver", "Pure Rust implementation of the Oracle protocol – nothing extra to install."),
            ("SQL and PL/SQL", "Scripts with PL/SQL blocks are split correctly."),
            ("Schemas and DDL", "Tables, views, columns, indexes and generated DDL."),
            ("Transactions", "Manual Commit / Rollback for careful work on production data."),
            ("Read-only & PROD tags", "Confirmation before every change on production connections."),
            ("Export", "Results to CSV and JSON, more formats in Pro."),
        ],
        "faq": [
            ("Do I need Oracle Instant Client?", "No. The driver is built into the app."),
            ("Which identifier do I enter – SID or service name?", "Use the service name, e.g. FREEPDB1 or ORCLPDB1."),
            ("Is Oracle support free?", "Yes, all database engines are available in the free version."),
        ],
    },
    {
        "slug": "snowflake-client-android",
        "name": "Snowflake",
        "title": "Snowflake Client for Android – SQL on Snowflake from Your Phone",
        "desc": "Snowflake client for Android: password, MFA (Duo push or passcode), browser SSO, PAT, OAuth and key-pair login. Pick warehouse, role, database and schema and run SQL.",
        "h1": "Snowflake client for Android",
        "lead": "Check a dashboard number, rerun a failed query or look at a table in Snowflake – right from your phone, with every login method your company uses.",
        "shot": "4-chart",
        "works": "Any Snowflake account (org-account identifier or account locator).",
        "steps": [
            "Tap <b>+ New</b> → <b>Snowflake</b> and enter your account identifier, e.g. <code>myorg-myaccount</code>.",
            "Choose the login method: password, password + MFA (Duo push or passcode), browser SSO, programmatic access token, OAuth or RSA key pair.",
            "Set warehouse, role, database and schema – the same context you use in Snowsight.",
            "Connect and run SQL; turn results into a bar or line chart with one tap.",
        ],
        "features": [
            ("Every login method", "Password, MFA, external browser SSO, PAT, OAuth token and key pair."),
            ("Warehouse & role", "Pick the context per connection."),
            ("Charts", "Bar and line charts from any query result."),
            ("Export", "Send results as CSV or JSON from the phone."),
            ("Read-only mode", "Protect production accounts from accidental changes."),
            ("Desktop layout", "Use DeX or a tablet for a full three-pane SQL IDE."),
        ],
        "faq": [
            ("Does SSO work on Android?", "Yes. External browser SSO opens your identity provider (Okta, Entra ID and others) in the browser to sign you in."),
            ("Can I use key-pair authentication?", "Yes. Paste the private key (optionally encrypted with a passphrase)."),
            ("Where are my credentials stored?", "Encrypted on the device with Android Keystore."),
        ],
    },
    {
        "slug": "mongodb-client-android",
        "name": "MongoDB",
        "title": "MongoDB Client for Android – mongosh Queries on Your Phone",
        "desc": "MongoDB client for Android with mongosh syntax. Connect to MongoDB Atlas (mongodb+srv), Azure Cosmos DB and Amazon DocumentDB, browse collections and run queries.",
        "h1": "MongoDB client for Android",
        "lead": "Query MongoDB and MongoDB Atlas from your phone using familiar mongosh syntax – find, aggregate, update – and see documents in a readable grid.",
        "shot": "1-connections",
        "works": "MongoDB, MongoDB Atlas (mongodb+srv://), Azure Cosmos DB for MongoDB and Amazon DocumentDB.",
        "steps": [
            "Tap <b>+ New</b> → <b>MongoDB</b> and paste your <code>mongodb+srv://</code> or <code>mongodb://</code> connection string.",
            "Enter the password (stored encrypted, not in the URL) and the default database.",
            "Connect – collections appear in the navigator.",
            "Run queries such as <code>db.orders.find({status: \"paid\"}).limit(20)</code> or an aggregation pipeline.",
        ],
        "features": [
            ("mongosh syntax", "find, aggregate, insert, update, delete – with ObjectId and ISODate support."),
            ("Atlas ready", "SRV connection strings work on Android."),
            ("Collections browser", "See collections and documents without writing a query."),
            ("Export", "Results to JSON or CSV."),
            ("PROD protection", "Confirmation before writes on production clusters."),
            ("One app for SQL and NoSQL", "The same app also talks to PostgreSQL, MySQL, Redis and more."),
        ],
        "faq": [
            ("Does it support MongoDB Atlas?", "Yes, including mongodb+srv connection strings."),
            ("Which query language does it use?", "mongosh (MongoDB Shell) syntax."),
            ("Is it free?", "Yes, MongoDB support is part of the free version."),
        ],
    },
    {
        "slug": "redis-client-android",
        "name": "Redis",
        "title": "Redis Client for Android – Browse Keys & Run Commands",
        "desc": "Redis client for Android: run redis-cli commands, browse keys grouped by type, connect to Redis Cloud, Upstash and Valkey with TLS.",
        "h1": "Redis client for Android",
        "lead": "Look into a cache, check a key or flush a stuck queue from your phone. Commands work like in redis-cli, and keys are grouped by type in the navigator.",
        "shot": "1-connections",
        "works": "Redis, Valkey, Redis Cloud and Upstash.",
        "steps": [
            "Tap <b>+ New</b> → <b>Redis</b>, or paste a <code>redis://</code> / <code>rediss://</code> URL.",
            "Enter host, port 6379, database number and password; enable TLS for Upstash or Redis Cloud.",
            "Connect – keys appear grouped by type (strings, hashes, lists, sets, sorted sets).",
            "Type one command per line, e.g. <code>GET session:42</code> or <code>HGETALL user:7</code>.",
        ],
        "features": [
            ("redis-cli style editor", "One command per line, results in a grid."),
            ("Keys by type", "Navigator groups keys so large databases stay readable."),
            ("TLS", "Works with managed Redis that requires encryption."),
            ("Write protection", "Write commands on PROD connections need confirmation."),
            ("Valkey & Upstash", "Same protocol, same app."),
            ("History", "Repeat recent commands with one tap."),
        ],
        "faq": [
            ("Does it work with Upstash?", "Yes – use the endpoint, port and password from the Upstash console with TLS enabled."),
            ("Can I use Valkey?", "Yes, Valkey is Redis-compatible."),
            ("Can I accidentally FLUSHALL production?", "Tag the connection PROD: every write command then asks for confirmation. Read-only mode blocks writes in the app."),
        ],
    },
    {
        "slug": "sqlite-browser-android",
        "name": "SQLite",
        "title": "SQLite Browser & Editor for Android – Open .db Files on Your Phone",
        "desc": "SQLite browser and editor for Android: open .db / .sqlite files, run SQL, edit rows, view the ER diagram, export CSV and JSON. Includes DuckDB for CSV and Parquet analytics.",
        "h1": "SQLite browser & editor for Android",
        "lead": "Open any SQLite database file on your phone, look at its tables, run SQL and fix data. Perfect for app developers inspecting a local database or anyone with a .db file to read.",
        "shot": "5-diagram",
        "works": "SQLite files (.db, .sqlite, .sqlite3) and DuckDB databases for analytics on CSV and Parquet.",
        "steps": [
            "Tap <b>Open database file</b> and pick a <code>.db</code> or <code>.sqlite</code> file – or create a new one.",
            "Not sure where to start? Tap <b>Create demo database</b> to get a sample shop with customers, orders and products.",
            "Browse tables, tap <b>Data</b> to see rows, or write your own SQL.",
            "Export results or make a backup copy of the database file.",
        ],
        "features": [
            ("Open any .db file", "Works with files from other apps, downloads or cloud storage."),
            ("Edit data", "Change, add and delete rows with an SQL preview."),
            ("Table designer", "Create tables with types and primary keys without writing DDL."),
            ("ER diagram (Pro)", "See tables and foreign keys at a glance."),
            ("DuckDB", "Analytical SQL on CSV and Parquet files, on the phone."),
            ("Backup & restore", "Copy the database file before risky changes."),
        ],
        "faq": [
            ("Can I open the SQLite database of another app?", "You can open any .db file you can access, for example one exported or downloaded to your device."),
            ("Does it work offline?", "Yes. Local SQLite and DuckDB files need no internet connection."),
            ("Is it free?", "Yes. Opening, querying and editing SQLite files is free."),
        ],
    },
]

GUIDES = [
    {
        "slug": "guides/ssh-tunnel-database-from-phone",
        "title": "How to Connect to a Private Database from Your Phone with an SSH Tunnel",
        "desc": "Step-by-step: reach a PostgreSQL, MySQL, SQL Server or Oracle database inside a private network from Android using an SSH tunnel through a bastion host.",
        "h1": "Connect to a private database from your phone with an SSH tunnel",
        "shot": "1-connections",
        "body": """
<p>Production databases usually are not exposed to the internet. They live in a private network and are reachable only from a <b>bastion</b> (jump) host. On a laptop you would run <code>ssh -L</code>; on Android TivaroSQL Studio does the same thing for you.</p>
<h2>What you need</h2>
<ul><li>An SSH host that can reach the database (e.g. <code>bastion.example.com</code>).</li><li>An SSH user with a password or a private key (OpenSSH, PKCS#8 or PuTTY .ppk).</li><li>Database host and port <i>as seen from the bastion</i> – often a private address such as <code>10.0.3.12:5432</code>.</li><li>TivaroSQL Studio Pro (the SSH tunnel is a Pro feature).</li></ul>
<h2>Step by step</h2>
<ol><li>Create a new connection for your engine (PostgreSQL, MySQL, SQL Server, Oracle or ClickHouse).</li><li>Enter the database host and port exactly as the bastion sees them.</li><li>Open the <b>SSH tunnel</b> section and enter the SSH host, port 22, user and password or key.</li><li>Tap <b>Test</b>. On the first connection the app shows the server's key fingerprint – compare it with your server and accept. Later connections verify the key automatically (trust on first use).</li><li>Tag the connection <b>PROD</b> and consider <b>read-only</b> mode for on-call work.</li></ol>
<h2>Security tips</h2>
<ul><li>Use a dedicated SSH key for the phone and remove it from <code>authorized_keys</code> if the phone is lost.</li><li>Use a database user with minimal privileges; for checks, a read-only role is enough.</li><li>Enable the app lock (fingerprint or PIN) for production connections.</li><li>Secrets are encrypted with Android Keystore and never leave the device.</li></ul>
""",
        "faq": [
            ("Is an SSH tunnel safer than opening the database port?", "Yes. The database stays private; only SSH is exposed and it can be limited to keys and specific users."),
            ("Why does TLS to ClickHouse fail through the tunnel?", "Through a tunnel the app connects to 127.0.0.1, so the certificate host name does not match. Use the tunnel without HTTPS or connect directly."),
        ],
    },
    {
        "slug": "guides/samsung-dex-sql-ide",
        "title": "Turn Your Phone into a SQL IDE with Samsung DeX or a USB-C Monitor",
        "desc": "Use an Android phone as a desktop SQL IDE: connect it to a monitor with Samsung DeX or USB-C and TivaroSQL Studio switches to a three-pane layout with navigator, editor and details.",
        "h1": "Your phone as a desktop SQL IDE (Samsung DeX, USB-C)",
        "shot": None,
        "body": """
<p>Modern phones are as fast as many laptops. Connect one to a monitor, add a keyboard and mouse, and TivaroSQL Studio turns into a desktop database IDE: navigator on the left, editor and results in the middle and table details on the right.</p>
<figure><img src="../../img/tablet-1-desktop.webp" width="1280" height="800" alt="TivaroSQL Studio desktop layout on Samsung DeX with navigator, SQL editor, results and table details" loading="lazy"></figure>
<h2>How to set it up</h2>
<ol><li>Connect the phone to a monitor with a USB-C to HDMI cable or dock (Samsung DeX), or wirelessly with DeX.</li><li>Pair a Bluetooth keyboard and mouse.</li><li>Open TivaroSQL Studio – from 900 px width the desktop layout appears automatically; from 1280 px you also get the details pane.</li><li>Use <b>Ctrl+Enter</b> to run the statement under the cursor and <b>Ctrl+Shift+Enter</b> to run the whole script.</li></ol>
<h2>What you get on the big screen</h2>
<ul><li>Connection tabs and query tabs side by side.</li><li>Resizable panes and automatic UI scaling (zoom with − / +).</li><li>Double-click a row to edit it, with SQL preview.</li><li>Status bar with server version, object count and last query time.</li></ul>
<p>The same layout works on Android tablets and Chromebooks.</p>
""",
        "faq": [
            ("Is the desktop layout a paid feature?", "No. The DeX / desktop layout is free."),
            ("Does it need Samsung DeX?", "No. Any Android device with a wide enough screen gets the desktop layout – tablets, Chromebooks and phones with desktop mode."),
        ],
    },
]

LANDING = {
    "en": {
        "path": APP,
        "lang": "en",
        "title": "TivaroSQL Studio – SQL & Database Client for Android",
        "desc": "Free SQL client for Android: PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, MongoDB, Redis, SQLite and 20+ databases. SQL editor, charts, ER diagram, SSH tunnel. No account, no tracking.",
        "eyebrow": "SQL & NoSQL client for Android",
        "h1": "Your databases.<br><em>In your pocket.</em>",
        "lead": "Connect to PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, MongoDB, Redis and 20+ other databases. Write SQL, browse tables and fix data from your phone – and get a full desktop IDE on Samsung DeX.",
        "cta": "Get it on Google Play",
        "cta2": "Supported databases",
        "trust": ["No account", "No ads, no tracking", "Passwords in Android Keystore"],
        "feat_h": "Everything you need to work with a database – on a phone",
        "features": [
            ("SQL editor", "Highlighting, table and column suggestions above the keyboard, formatter, query tabs, history and templates."),
            ("Data grid", "Sort, filter, export to CSV / JSON / Excel. Edit rows with an SQL preview before saving."),
            ("Charts", "Turn any query into a bar or line chart with one tap."),
            ("ER diagram & EXPLAIN", "See your schema at a glance and find slow queries with readable plans."),
            ("Safe on production", "DEV / TEST / PROD tags, read-only mode, confirmation before changes, fingerprint lock."),
            ("Desktop on DeX", "Plug in a monitor for a three-pane IDE: navigator, editor and details."),
        ],
        "db_h": "20+ databases and clouds",
        "shots_h": "Screenshots",
        "pricing_h": "Free and Pro",
        "pricing": "Running SQL, browsing and editing tables, every database engine and the desktop layout are free. <b>Pro</b> – a one-time purchase or a monthly subscription – unlocks unlimited connections, tabs and history, SSH tunnel, ER diagram, EXPLAIN, schema compare, import and all export formats.",
        "faq_h": "Frequently asked questions",
        "faq": [
            ("Is TivaroSQL Studio free?", "Yes. The app is free to download and the core features are free. Pro is optional."),
            ("Which databases are supported?", "PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SQLite, DuckDB, ClickHouse, Snowflake, Turso, MongoDB, Redis, Cassandra and compatible cloud services such as Neon, Supabase, PlanetScale, Azure SQL and Amazon RDS."),
            ("Does my data go through your servers?", "No. The phone connects directly to the database you choose. There is no account, no analytics and no tracking."),
            ("Is it safe to use on production?", "Mark connections as PROD to confirm every change, use read-only mode and lock the app or single connections with a fingerprint or PIN."),
            ("Is there an iPhone version?", "Not yet – TivaroSQL Studio is available for Android."),
        ],
        "guides_h": "Guides",
        "other": ("Polski", "pl/"),
    },
    "pl": {
        "path": APP + "pl/",
        "lang": "pl",
        "title": "TivaroSQL Studio – klient SQL i baz danych na Androida",
        "desc": "Darmowy klient SQL na Androida: PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, MongoDB, Redis, SQLite i ponad 20 baz. Edytor SQL, wykresy, diagram ER, tunel SSH. Bez konta i śledzenia.",
        "eyebrow": "Klient SQL i NoSQL na Androida",
        "h1": "Twoje bazy danych.<br><em>W kieszeni.</em>",
        "lead": "Połącz się z PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, MongoDB, Redis i ponad 20 innymi bazami. Pisz SQL, przeglądaj tabele i poprawiaj dane z telefonu – a na Samsung DeX masz pełne środowisko jak na komputerze.",
        "cta": "Pobierz z Google Play",
        "cta2": "Obsługiwane bazy",
        "trust": ["Bez konta", "Bez reklam i śledzenia", "Hasła w Android Keystore"],
        "feat_h": "Wszystko, czego potrzebujesz do pracy z bazą – na telefonie",
        "features": [
            ("Edytor SQL", "Kolorowanie składni, podpowiedzi tabel i kolumn nad klawiaturą, formatowanie, karty, historia i szablony."),
            ("Siatka danych", "Sortowanie, filtrowanie, eksport do CSV / JSON / Excela. Edycja wierszy z podglądem SQL przed zapisem."),
            ("Wykresy", "Każde zapytanie jako wykres słupkowy lub liniowy jednym stuknięciem."),
            ("Diagram ER i EXPLAIN", "Cały schemat na jednym ekranie i czytelne plany zapytań."),
            ("Bezpiecznie na produkcji", "Znaczniki DEV / TEST / PROD, tryb tylko do odczytu, potwierdzanie zmian, blokada odciskiem palca."),
            ("Komputer na DeX", "Podłącz monitor i pracuj w układzie trzech paneli: nawigator, edytor, szczegóły."),
        ],
        "db_h": "Ponad 20 baz danych i chmur",
        "shots_h": "Zrzuty ekranu",
        "pricing_h": "Wersja darmowa i Pro",
        "pricing": "Wykonywanie SQL, przeglądanie i edycja tabel, wszystkie silniki baz i układ desktopowy są za darmo. <b>Pro</b> – jednorazowo albo w subskrypcji miesięcznej – odblokowuje nielimitowane połączenia, karty i historię, tunel SSH, diagram ER, EXPLAIN, porównanie schematów, import i wszystkie formaty eksportu.",
        "faq_h": "Najczęstsze pytania",
        "faq": [
            ("Czy TivaroSQL Studio jest darmowe?", "Tak. Aplikację pobierasz za darmo, a podstawowe funkcje są bezpłatne. Pro jest opcjonalne."),
            ("Jakie bazy są obsługiwane?", "PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SQLite, DuckDB, ClickHouse, Snowflake, Turso, MongoDB, Redis, Cassandra oraz zgodne usługi chmurowe: Neon, Supabase, PlanetScale, Azure SQL, Amazon RDS."),
            ("Czy moje dane przechodzą przez Wasze serwery?", "Nie. Telefon łączy się bezpośrednio z wybraną bazą. Nie ma konta, analityki ani śledzenia."),
            ("Czy to bezpieczne na produkcji?", "Oznacz połączenie jako PROD (potwierdzenie każdej zmiany), włącz tryb tylko do odczytu i blokadę odciskiem palca lub PIN-em."),
            ("Jaki jest język aplikacji?", "Interfejs jest obecnie po angielsku."),
        ],
        "guides_h": "Poradniki (EN)",
        "other": ("English", "../"),
    },
}

SHOTS = [
    ("1-connections", "Connection list with PostgreSQL, Snowflake, MySQL, MongoDB, Redis and SQL Server"),
    ("2-editor", "SQL editor with syntax highlighting on Android"),
    ("3-results", "Query results grid on Android"),
    ("4-chart", "Bar chart created from an SQL query"),
    ("5-diagram", "Interactive ER diagram of a database"),
    ("6-edit", "Editing a table row with type information"),
    ("7-plan", "EXPLAIN query plan with a full scan warning"),
    ("8-drivers", "Choosing a database driver or pasting a JDBC URL"),
]

DB_LIST = ["PostgreSQL", "MySQL", "MariaDB", "SQL Server", "Oracle", "SQLite", "DuckDB", "ClickHouse", "Snowflake",
           "MongoDB", "Redis", "Cassandra", "Neon", "Supabase", "PlanetScale", "TiDB", "CockroachDB", "Amazon RDS",
           "Amazon Redshift", "Azure SQL", "Turso", "Valkey", "Upstash", "Firebird"]


# ---------------------------------------------------------------- HTML helpers
def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def app_ld(lang):
    return {
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": "TivaroSQL Studio",
        "operatingSystem": "Android", "applicationCategory": "DeveloperApplication",
        "description": LANDING[lang]["desc"], "url": BASE + LANDING[lang]["path"], "downloadUrl": PLAY,
        "image": BASE + APP + "img/feature-graphic.png", "inLanguage": "en",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "publisher": {"@type": "Organization", "name": "Tivaroid Studio", "url": BASE + "/"},
    }


def faq_ld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (n, u) in enumerate(items)]}


def rel(path, target):
    """Relative link from page `path` (dir ending in /) to site path `target`."""
    depth = path.strip("/").count("/") + 1 if path.strip("/") else 0
    return "../" * depth + target.lstrip("/")


def head(path, title, desc, lang="en", alternates=None, ld=()):
    canon = BASE + path
    alt = ""
    for hl, p in (alternates or {}).items():
        alt += f'<link rel="alternate" hreflang="{hl}" href="{BASE + p}">'
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">{alt}
<meta name="theme-color" content="#0b0f14"><meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website"><meta property="og:site_name" content="TivaroSQL Studio">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{BASE + APP}img/feature-graphic.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{rel(path, '/assets/icons/tivarosqlstudio.svg')}" type="image/svg+xml">
<link rel="stylesheet" href="{rel(path, APP + 'sql.css')}">
{''.join(jsonld(x) for x in ld)}
</head><body>"""


def nav(path, lang="en"):
    r = lambda t: rel(path, t)
    home_txt = "Bazy" if lang == "pl" else "Databases"
    return f"""<header class="top"><div class="wrap nav">
<a class="brand" href="{r(APP if lang == 'en' else APP + 'pl/')}"><img src="{r('/assets/icons/tivarosqlstudio.svg')}" width="28" height="28" alt=""><b>Tivaro<span>SQL</span> Studio</b></a>
<nav><a href="{r(APP)}#databases">{home_txt}</a><a href="{r(APP)}#guides">Guides</a><a class="btn small" href="{play('nav')}" rel="noopener">Google Play</a></nav>
</div></header>"""


def footer(path):
    r = lambda t: rel(path, t)
    links = "".join(f'<a href="{r(APP + p["slug"] + "/")}">{p["name"]} client for Android</a>' for p in PAGES)
    guides = "".join(f'<a href="{r(APP + g["slug"] + "/")}">{esc(g["h1"])}</a>' for g in GUIDES)
    return f"""<footer class="foot"><div class="wrap cols">
<div><b>TivaroSQL Studio</b><p>SQL &amp; NoSQL database client for Android by <a href="{r('/')}">Tivaroid Studio</a>.</p>
<p><a href="{r('/tivarosqlstudio-privacy/')}">Privacy policy</a> · <a href="mailto:tivaroid.studio@gmail.com">Contact</a></p></div>
<div><b>Databases</b>{links}</div><div><b>Guides</b>{guides}<a href="{r(APP + 'pl/')}">TivaroSQL Studio po polsku</a></div>
</div><div class="wrap copy">© {datetime.date.today().year} Tivaroid Studio · Google Play and the Google Play logo are trademarks of Google LLC.</div></footer></body></html>"""


def play_btn(campaign, label="Get it on Google Play"):
    return f'<a class="btn" href="{play(campaign)}" rel="noopener">▶ {esc(label)}</a>'


def faq_html(faq, h="Frequently asked questions"):
    items = "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq)
    return f'<section class="wrap"><h2>{esc(h)}</h2><div class="faq">{items}</div></section>'


def write(path, content):
    f = ROOT / path.lstrip("/") / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content)


# ---------------------------------------------------------------- pages
def landing(lang):
    L = LANDING[lang]
    path = L["path"]
    r = lambda t: rel(path, t)
    feats = "".join(f'<div class="card"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in L["features"])
    dbs = "".join(
        (f'<a class="chip" href="{r(APP + p["slug"] + "/")}">{d}</a>' if (p := next((x for x in PAGES if x["name"] == d), None))
         else f'<span class="chip">{d}</span>') for d in DB_LIST)
    shots = "".join(f'<img src="{r(APP + "img/" + k + ".webp")}" width="540" height="960" alt="{esc(a)}" loading="lazy">' for k, a in SHOTS)
    guides = "".join(f'<a class="card link" href="{r(APP + g["slug"] + "/")}"><h3>{esc(g["h1"])}</h3><p>{esc(g["desc"])}</p></a>' for g in GUIDES)
    trust = "".join(f"<li>✓ {esc(t)}</li>" for t in L["trust"])
    body = f"""{nav(path, lang)}<main>
<section class="hero wrap"><div><div class="eyebrow">{esc(L['eyebrow'])}</div><h1>{L['h1']}</h1><p class="lead">{esc(L['lead'])}</p>
<div class="actions">{play_btn('landing_' + lang, L['cta'])}<a class="btn ghost" href="#databases">{esc(L['cta2'])}</a></div>
<ul class="trust">{trust}</ul><p class="langs"><a href="{L['other'][1]}" hreflang="{'pl' if lang == 'en' else 'en'}">{L['other'][0]}</a></p></div>
<img class="hero-shot" src="{r(APP + 'img/1-connections.webp')}" width="540" height="960" alt="TivaroSQL Studio connection list on an Android phone"></section>
<section class="wrap"><h2>{esc(L['feat_h'])}</h2><div class="grid">{feats}</div></section>
<section class="wrap" id="databases"><h2>{esc(L['db_h'])}</h2><div class="chips">{dbs}</div></section>
<section class="wrap"><h2>{esc(L['shots_h'])}</h2><div class="shots">{shots}</div></section>
<section class="wrap"><h2>{esc(L['pricing_h'])}</h2><p class="prose">{L['pricing']}</p><div class="actions">{play_btn('pricing_' + lang, L['cta'])}</div></section>
<section class="wrap" id="guides"><h2>{esc(L['guides_h'])}</h2><div class="grid two">{guides}</div></section>
{faq_html(L['faq'], L['faq_h'])}</main>{footer(path)}"""
    alts = {"en": APP, "pl": APP + "pl/", "x-default": APP}
    write(path, head(path, L["title"], L["desc"], L["lang"], alts, [app_ld(lang), faq_ld(L["faq"])]) + body)


def engine(p):
    path = APP + p["slug"] + "/"
    r = lambda t: rel(path, t)
    steps = "".join(f"<li>{s}</li>" for s in p["steps"])
    feats = "".join(f'<div class="card"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for t, d in p["features"])
    others = "".join(f'<a class="chip" href="{r(APP + x["slug"] + "/")}">{x["name"]}</a>' for x in PAGES if x is not p)
    body = f"""{nav(path)}<main>
<nav class="wrap crumbs"><a href="{r(APP)}">TivaroSQL Studio</a> › {esc(p['name'])}</nav>
<section class="hero wrap"><div><div class="eyebrow">{esc(p['name'])} · Android</div><h1>{esc(p['h1'])}</h1><p class="lead">{esc(p['lead'])}</p>
<div class="actions">{play_btn(p['slug'])}</div><p class="note">Works with: {esc(p['works'])}</p></div>
<img class="hero-shot" src="{r(APP + 'img/' + p['shot'] + '.webp')}" width="540" height="960" alt="{esc(p['name'])} client for Android – TivaroSQL Studio screenshot"></section>
<section class="wrap"><h2>How to connect to {esc(p['name'])} from Android</h2><ol class="steps">{steps}</ol></section>
<section class="wrap"><h2>What you can do</h2><div class="grid">{feats}</div></section>
<section class="wrap"><h2>Private and safe by design</h2><p class="prose">TivaroSQL Studio connects directly from your phone to {esc(p['name'])} – there is no proxy server and no account. Passwords and keys are encrypted with Android Keystore, the app has no ads, analytics or tracking, and you can lock it or a single connection with your fingerprint.</p></section>
{faq_html(p['faq'])}
<section class="wrap"><h2>Other databases</h2><div class="chips">{others}</div><div class="actions">{play_btn(p['slug'] + '_bottom')}</div></section>
</main>{footer(path)}"""
    ld = [app_ld("en"), faq_ld(p["faq"]), crumbs_ld([("TivaroSQL Studio", APP), (p["name"], path)])]
    write(path, head(path, p["title"], p["desc"], ld=ld) + body)


def guide(g):
    path = APP + g["slug"] + "/"
    r = lambda t: rel(path, t)
    shot = f'<img class="hero-shot" src="{r(APP + "img/" + g["shot"] + ".webp")}" width="540" height="960" alt="TivaroSQL Studio on Android">' if g["shot"] else ""
    article = {"@context": "https://schema.org", "@type": "TechArticle", "headline": g["h1"], "description": g["desc"],
               "dateModified": TODAY, "author": {"@type": "Organization", "name": "Tivaroid Studio"},
               "mainEntityOfPage": BASE + path, "image": BASE + APP + "img/feature-graphic.png"}
    body = f"""{nav(path)}<main>
<nav class="wrap crumbs"><a href="{r(APP)}">TivaroSQL Studio</a> › Guides</nav>
<article class="wrap guide"><div class="eyebrow">Guide</div><h1>{esc(g['h1'])}</h1><p class="note">Updated {TODAY}</p>
<div class="guide-body"><div class="prose">{g['body']}</div>{shot}</div><div class="actions">{play_btn(g['slug'].split('/')[-1])}</div></article>
{faq_html(g['faq'])}</main>{footer(path)}"""
    ld = [article, faq_ld(g["faq"]), crumbs_ld([("TivaroSQL Studio", APP), ("Guides", APP + "#guides"), (g["h1"], path)])]
    write(path, head(path, g["title"], g["desc"], ld=ld) + body)


def sitemap():
    urls = ["/", APP, APP + "pl/"] + [APP + p["slug"] + "/" for p in PAGES] + [APP + g["slug"] + "/" for g in GUIDES]
    urls += ["/tivarosqlstudio-privacy/"]
    body = "".join(f"<url><loc>{BASE + u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{body}</urlset>\n')
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")


def privacy_redirect():
    # The app (src/lib/appInfo.ts → PRIVACY_URL) links to /TivaroSQLStudio/privacy-policy – keep that URL alive.
    target = BASE + "/tivarosqlstudio-privacy/"
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>TivaroSQL Studio Privacy Policy</title>
<link rel="canonical" href="{target}"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0; url={target}">
</head><body><p>The privacy policy has moved: <a href="{target}">{target}</a></p></body></html>"""
    d = ROOT / "TivaroSQLStudio"
    d.mkdir(exist_ok=True)
    (d / "privacy-policy.html").write_text(page)
    (d / "privacy-policy").mkdir(exist_ok=True)
    (d / "privacy-policy" / "index.html").write_text(page)


if __name__ == "__main__":
    for lang in LANDING:
        landing(lang)
    for p in PAGES:
        engine(p)
    for g in GUIDES:
        guide(g)
    sitemap()
    privacy_redirect()
    print("ok")
