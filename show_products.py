'''
description:
https://www.codewars.com/kata/545cff101288c1d2da0006fb
'''
def pagination_text(page_number, page_size, total_products):
    s=""
    if page_number<=(total_products//page_size):
        s= "Showing %d to %d of %d Products." % (1+(page_number-1)*page_size, page_size*page_number, total_products)
    elif page_number>(total_products//page_size):
        s=( "Showing %d to %d of %d Products." % (1+(page_number-1)*page_size, total_products, total_products))
    return s
