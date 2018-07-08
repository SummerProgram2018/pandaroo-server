import json

def get_configuration(path, environ): 

    with open('config.json', 'r') as f:
        config = json.load(f)

    if environ == 'DEFAULT': 
	return config[environ]

    config = config[environ] 
    config_keys = config.keys()
    default_keys = [key for key in config["DEFAULT"].keys() if key not in config.keys()] 
    
    for dkey in default_keys: 
        config[dkey] = config['DEFAULT'][dkey]

    return config


