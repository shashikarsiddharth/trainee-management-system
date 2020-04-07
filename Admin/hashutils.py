import hashlib

def make_pwd_hash(password):
    ''' Function that takes a password and converts it into a hash before storing it into the database. '''
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_pwd_hash(password, hash):
    ''' Function that checks password and the corresponding hash based on the username. '''   
    if make_pwd_hash(password) == hash:
        return True
    return False
