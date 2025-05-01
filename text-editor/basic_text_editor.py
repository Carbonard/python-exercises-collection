from text_editor_functions import *

# directory = "files"
# file_name = "prueba.txt"
src = FileManager()

options={
    'help' : lambda _: Help(),
    'rf' : read_file,
    'wf' : write_file,
    'df' : delete_content,
    'cf' : lambda _: src.change_file_name(),
    'cd' : lambda _: src.change_directory(),
    'vf' : view_files
}

while True:
    option = input(f"""\nCurrent file is {src.file_name} in {src.directory}.
                   
What do you what to do?
""").lower().strip()
    if not option:
        continue
    option = option.split(' ')
    # If exit demanded
    if option[0] in {'exit','e'}:
        break
    # Simplifying given option to two letters
    if len(option)==1:
        option = option[0]
    else:
        # Get first letters from first two words
        option = option[0][0]+option[1][0]
    # Doing actions
    try:
        options[option](src)
    except KeyError:
        print("invalid option.")
        Help()
        continue