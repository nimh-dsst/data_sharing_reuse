import nltk
from nltk.corpus import wordnet

import re

def syns(doc):
    syns = []
    for w in nltk.tokenize.word_tokenize(doc):
        for syn in wordnet.synsets(w):
            syns.extend([l.name() for l in syn.lemmas()])
    return(' '.join(list(set(syns))))

def sep_urls(doc):
    return(doc.replace('/', ' '))

def check_paren(myStr): 
    open_list = ["[","{","("] 
    close_list = ["]","}",")"] 
    stack = [] 
    parentheses = 0
    for i in myStr: 
        if i in open_list: 
            parentheses = 1
            stack.append(i) 
        elif i in close_list: 
            parentheses = 1
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0 and parentheses == 1: 
        return "Balanced"
    
    if len(stack) > 0 and parentheses == 1:
        return "Unbalanced"
    
    if parentheses == 0:
        return 'No Parentheses'
    
def repo_label(text):
    passage_marked = 0
    
    reg_matches = re.compile(r"""(github)|(osf\.io)|(nda\.nih\.gov)|(openneuro)|(\sndar)|(\(ndar\))|
                                 (national database for autism research)|(brain-map\.org)|
                                 (humanconnectome\.org)|(balsa\.wustl\.edu)|(loni\.usc\.edu)|
                                 (ida\.loni\.usc\.edu)|(fmridc)|(ccrns)|(datalad)|(dataverse)|
                                 (dbgap)|(nih\.gov\/gap)|(dryad)|(figshare)|(fcon_1000\.projects)|
                                 (nitrc)|(mcgill\.ca\/bic\/resources\/omega)|(xnat\.org)|
                                 (zenodo)|(opendata\.aws)""", re.X|re.VERBOSE)
    
    m = re.search(reg_matches, text.lower())
    if m:
        return(m.group())
    else:
        return('no_repo_mentioned')
