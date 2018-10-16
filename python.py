def git_next_targit(page) :
    start_link=page.find('<a href=')
    if start_link==-1:
        return None,0
    stat_quote=page.find('"',start_page)
    end_quot=page.find('"',statr_quot+1)
    url=page[start_quot+1:end_quote]
    return url,end_quote
