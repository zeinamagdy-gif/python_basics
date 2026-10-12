test_settings={'theme': 'light',"notifications":"enabled", 'language': 'English'}
# settings = 
def add_setting(test_settings, pair):
    key,value=pair
    key = key.lower()
    value = value.lower()

    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    test_settings[key] = value

    return( f"Setting '{key}' added with value '{value}' successfully!")

def update_setting(test_settings, pair):
    key,value=pair
    key = key.lower()
    value = value.lower()
    if key in test_settings:
       test_settings[key]=value
       return(f"Setting '{key}' updated to '{value}' successfully!") 
    return(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")
def delete_setting(test_settings, key):
    
    key = key.lower()
    
    if key in test_settings:
        del test_settings[key]
        return (f"Setting '{key}' deleted successfully!")
    return ("Setting not found!")
def view_settings(test_settings):
    if not test_settings:
        return "No settings available."
    result= "Current User Settings:\n"
    for key,value in test_settings.items():
        result+=f"{key.capitalize()}: {value}\n"
    return result
    


print(add_setting(test_settings, ('THEME', 'dark')))
# Setting 'theme' already exists! Cannot add a new setting with this name.

print(add_setting(test_settings, ('VOLUME', 'HIGH')))
# Setting 'volume' added with value 'high' successfully!

print(update_setting(test_settings, ('LANGUAGE', 'ARABIC')))
# Setting 'language' updated to 'arabic' successfully!

print(delete_setting(test_settings, 'VOLUME'))
# Setting 'volume' deleted successfully!
settings={}
print(view_settings(settings))
print(view_settings(test_settings))

