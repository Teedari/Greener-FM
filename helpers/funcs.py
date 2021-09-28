import uuid


def generate_username_code():
  return str(uuid.uuid4().int)[:5]

def separate_fullname(name):
  first_name = ''
  last_name = ''
  isFirstSpace = False
  for char in name:
    if isFirstSpace:
      last_name+= char
      continue
    
    if char == ' ':
      isFirstSpace=True
      
    first_name+= char
    
  return {'first_name': first_name.strip(), 'last_name': last_name.strip()}
      
    