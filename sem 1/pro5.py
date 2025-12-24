def update_visted_link(visited,new_link):

    
    set_new_link =set(new_link) 
    true_visted=set_new_link-visited
    count=len(true_visted)
    
    coimbained= set_new_link|visited
    final_tuple=tuple(coimbained)
    return(final_tuple,count)
visited = {'http://example.com', 'http://google.com', 'http://test.com'}
new_link = ['http://google.com', 'http://python.org', 'http://example.com/about', 'http://test.com']
print(update_visted_link(visited,new_link))