def return_passages(r_out):
    out_dat = []
    
    try:
        tmp_doi = r_out['documents'][0]['passages'][0]['infons']['article-id_doi']
    except:
        tmp_doi = None
    try:
        tmp_pmcid = r_out['documents'][0]['id']
    except:
        tmp_pmcid = None
        
    for passage in r_out['documents'][0]['passages']:
        if test_suitability:
            try:
                section_type = passage['infons']['section_type']
            except:
                section_type=None
                
            out_dat.append([passage['text'],
                           passage['offset'],
                           tmp_pmcid,
                           tmp_doi,
                           section_type])
        
    return(out_dat)

def test_suitability(passage):
    #figures out whether a passage is suitable for what we're after.
    #probably still needs some fiddling.
    suitability = True
    try:
        if passage['infons']['section_type'].lower() == 'ref':
            suitability = False

        if passage['infons']['type'].lower() == 'table':
            suitability = False

        if 'title' in passage['infons']['type'].lower():
            suitability = False
    except:
        suitability = False
    
    return(suitability)
