I am only interested in documents with the type of 'votering'. 




# Models
## The person table. 
    CREATE TABLE person (
    id int,
    hangar_id int, # what?
    intressent_id varchar(20),
    kontrollsumma varchar(50),
    född_år smallint,
    född datetime,
    avliden datetime,
    kön varchar(6),
    förnamn varchar(50),
    efternamn nvarchar(50),
    tilltalsnamn nvarchar(50),
    sorteringsnamn varchar(80),
    iort varchar(40),
    parti varchar(40),
    valkrets varchar(50),
    bänknummer int,
    invalsordning int,
    status varchar(100),
    källa varchar(20),
    källa_id varchar(40),
    statsråd varchar(50),
    timestamp datetime,
    personid int
    );

intressent_id is the foreign key relationship between several tables. 

Check whether a person has been an MP. 
PersonCommitment -> role_code == Riksdagsledamot && tom == 2014-09-29

### person
hangar_guid
intressent_id

### personuppdrag
organ_sortering
uppdrag_rollsortering
uppdrag_statussortering
status? tjänstgörande / null
lista på organ?

## Dokument table

    CREATE TABLE dokument (
    hangar_id int,
    dok_id nvarchar(255),
    rm nvarchar(255),
    beteckning nvarchar(255),
    doktyp nvarchar(255),
    typ nvarchar(255),
    subtyp nvarchar(255),
    tempbeteckning nvarchar(255),
    organ nvarchar(255),
    mottagare nvarchar(255),
    nummer int,
    slutnummer int,
    datum datetime,
    systemdatum datetime,
    publicerad datetime,
    titel nvarchar(255),
    subtitel nvarchar(255),
    status nvarchar(255),
    htmlformat nvarchar(255),
    relaterat_id nvarchar(255),
    source nvarchar(255),
    sourceid nvarchar(255),
    dokument_url_text nvarchar(255),
    dokument_url_html nvarchar(255),
    dokumentstatus_url_xml nvarchar(255),
    utskottsforslag_url_xml nvarchar(255),
    html ntext
    );

### dokument
rm? riksmöte. 
beteckning -> lista på beteckningar?

## Nedan votering? Utskottsforslag. 
    CREATE TABLE dokutskottsforslag (
    rm nvarchar(255),
    bet nvarchar(255),
    punkt int,
    beteckning nvarchar(255),
    rubrik nvarchar(255),
    forslag nvarchar(255),
    forslag_del2 nvarchar(255),
    beslutstyp nvarchar(255),
    beslut nvarchar(255),
    motforslag_nummer int,
    motforslag_partier nvarchar(255),
    votering_id nvarchar(255),
    votering_sammanfattning_html nvarchar(255),
    votering_ledamot_url_xml nvarchar(255),
    vinnare nvarchar(255)
    );
punkt? 

Måste maskinläsa voteringar via scraping. 

## Organ
    CREATE TABLE organ (
    id int,
    kod varchar(50),
    namn varchar(100),
    typ varchar(50),
    status varchar(12),
    sortering int,
    namn_en varchar(100),
    domän varchar(50),
    beskrivning varchar(1000)
    );

kod = used as a foreign key in some way. 
beskrivning = riktiga namnet. 