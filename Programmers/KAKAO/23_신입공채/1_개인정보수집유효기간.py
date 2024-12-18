def solution(today, terms, privacies):
    term2month = create_term2month(terms)
    
    answer = []
    return answer

def create_term2month(terms):
    term2month = {}
    for term in terms:
        term, month = term.split()
        term2month[term] = int(month)
    return term2month