I am only interested in documents with the type of 'votering'. 

hangar_id is the thing that connects everything. 


# Models
## The person table. 
    CREATE TABLE person (
    id int,
    hangar_id int, # what? hangar
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
hangar_id is the id for documents. 
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
    Binder samman alla dokumentdelar
    
    dok_id nvarchar(255),
    [dok_id](http://data.riksdagen.se/Dokumentation/Sa-funkar-dokument-id/)Består av kod för riksmöte, dokumentserie, dokumentbeteckning
    
    rm nvarchar(255),
    riksmöte, ett riksdagsår tex 2010/2011
    
    beteckning nvarchar(255),
    Sista delen i dok_id, beteckning på dokument. Bestående av [utskott](http://data.riksdagen.se/sv/koder/?typ=organ&utformat=html) och siffra tex AU10
    
    doktyp nvarchar(255),
    Typ av dokument [lista här](http://data.riksdagen.se/Dokumentation/Koder-och-termer/)
    
    typ nvarchar(255),
    typ av dokument, se [kodnyckel](http://data.riksdagen.se/sv/koder/?typ=doktyp&utformat=html) tex bet -> betänkande
    
    subtyp nvarchar(255),
    subtyp av dokument, se [kodnyckel](http://data.riksdagen.se/sv/koder/?typ=doktyp&utformat=html), tex prop -> proposition
    
    tempbeteckning nvarchar(255),
    ?? används när?
    
    organ nvarchar(255),
    utskott och organ?, se [kodnyckel](http://data.riksdagen.se/sv/koder/?typ=organ&utformat=html) tex AU -> Arbetsmarknadsutskottet
    
    mottagare nvarchar(255),
    ??
    
    nummer int,
    ?? 
    
    slutnummer int,
    ??
    
    datum date,
    Datum är datum för dokument utan tid. 
    
    systemdatum datetime,
    ??
    
    publicerad datetime,
    tid när det publiceras på ...
    
    titel nvarchar(255),
    titel på dokument
    
    subtitel nvarchar(255),
    undertitel på dokument
    
    status nvarchar(255),
    ?? 
    
    htmlformat nvarchar(255),
    ?? 
    
    relaterat_id nvarchar(255),
    ??
    
    source nvarchar(255),
    ??
    
    sourceid nvarchar(255),
    ??
    
    dokument_url_text nvarchar(255),
    länk till data.riksdag.se med dokument i råtext
    
    dokument_url_html nvarchar(255),
    länk till data.riksdag.se med dokument i html
    
    dokumentstatus_url_xml nvarchar(255),
    länk till data.riksdag.se med dokaktivitet i xml
    
    utskottsforslag_url_xml nvarchar(255),
    länk till data.riksdag.se med utskottsforslag i xml
    
    html ntext
    dokumentet i xml
    );

## Votering table
hangar_id -> id for dokument.
votering > huvud ? what does it pertain. 
beteckning. 

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