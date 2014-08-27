import sys
import re
import os

PERSON_DIC = { 'person':
        [ ('person', 'riksdagen_person'),
        ('född_år', 'born_year'),
        ('kön', 'sex'),
        ('efternamn', 'lastname'),
        ('tilltalsnamn', 'firstname'),
        ('sorteringsnamn', 'sort_name'),
        ('parti', 'party'),
        ('valkrets', 'constituency')],

        'personuppdrag': [
        ('personuppdrag', 'riksdagen_personcommitment'),
        ('roll_kod', 'role_code'),
        ('ordningsnummer', 'seq_nr'),
        ('typ', 'type_of'),
        ('[from]', 'from_date'),
        ('tom', 'until'),
        ('uppgift', 'task'),
        ('intressent_id', 'fk_personcommitment_person_id')],

        'personuppgift': [
        ('personuppgift', 'riksdagen_personalrecord'),
        ('uppgift_kod', 'record_name'),
        ('uppgift', 'record'),
        ('uppgift_typ', 'record_type'),
        ('intressent_id', 'fk_personalrecord_person_id')],

        'votering': [
        ('votering', 'riksdagen_voting'),
        ('rm', 'party_year'),
        ('beteckning', 'label'),
        ('hangar_id', 'hangar_id'), # should be hangar_id
        ('votering_id', 'voting_id'),
        ('punkt', 'doc_item'),
        ('intressent_id', 'fk_voting_person_id'),
        ('rost', 'vote'),
        ('avser', 'pertaining'),
        ('votering', 'voting_part'),
        ('banknummer', 'desk_nr'),
        ('datum', 'date')],

        # labels used as doktyp, rm:beteckning
        # Organ plus siffra is beteckning.

        'dokument': [
        ('INTO dokument', 'INTO document'),
        ('dok_id', 'doc_id'),
        ('rm', 'party_year'),
        ('beteckning', 'label'), # where can you find all the labels
        ('doktyp', 'doctype'),
        ('typ', 'type'),
        ('subtyp', 'subtype'),
        ('tempbeteckning', 'templabel'), # empty
        ('organ', 'govorgan'),
        ('mottagare', 'reciever'), #empty
        ('nummer', 'number'), # what?
        ('slutnummer', 'endnumber'),
        ('datum', 'date'),
        ('sytemdatum', 'system_date'),
        ('publicerad', 'publicised'), # not different from system_date
        ('titel', 'title'),
        ('subtitel', 'subtitle'),
        ('status', 'status'),
        ('relaterat_id', 'related_id'), # empty
        ('source', 'source'), # empty
        ('sourceid', 'sourceid'),
        ('dokument_url_text', 'document_url_text'),
        ('dokument_url_html', 'document_url_html'),
        ('dokumentstatus_url_xml', 'documentstatus_url_xml'), # xml for docactivity
        ('utskottsforslag_url_xml', 'committee_prop_url_xml'),
        ('html', 'html'),
        ]
    }

######## Helpers to check_replace #######

def find_whole_word(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def replace(string, name):
    for original, replace in PERSON_DIC[name]: #
        #print(original, replace)
        if find_whole_word(original)(string):
            string = string.replace(original, replace, 1)
    return string

def outputfile(string):
    with open('output.sql', 'a') as f:
        f.write(string+'\n')

def get_name(string):
    splitted = string.split()
    # print(splitted) # capture the first line for debugging
    return splitted[2]

def word_exist(wordlist, string):
    for w in wordlist:
        if find_whole_word(w)(string):
            return True
    return False

############### end of helpers #############

def check_replace(string, table_word_list):
    if word_exist(table_word_list, string):
        return '' # ignore sqlblock with these tables.
    else:
        name = get_name(string)
        string = replace(string, name)
        outputfile(string)
        return ''

def main(filename, table_word_list):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        string = ''
        for line in f:
            if ';' in line:
                string = string + line
                string = check_replace(string, table_word_list)
            elif line != '\n':
                string = string + line

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Please include an input filename")
    else:
        filename = sys.argv[1]
        table_word_list = sys.argv[2:]
    if os.path.exists('output.sql'):
        os.truncate('output.sql', 0)
    main(filename, table_word_list)


