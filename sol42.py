def display_info(name, section, rollno='03'):# default argument
    data = f'''   
    Name    : {name}
    section : {section}
    roll no : {rollno}
    '''    
    return data
out = display_info('Aditya tiwari','cd(I)')
print(out)
