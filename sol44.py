#arbitrary keywords

def display_info(**dct):# default argument    
    data = f'''   
    Name    : {dct["name"]}
    section : {dct['section']}
    roll no : {dct.get('rolln')}
    mobile : {dct.get('mobile')}
    '''    
    return data

out = display_info(section = 'cd' , name = 'Aditya tiwari', mobile = "888888888")
print(out)
