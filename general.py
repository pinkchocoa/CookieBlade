import os

# Each website is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt') 
    crawled = os.path.join(project_name,"crawled.txt")
    result = os.path.join(project_name,"result.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(result):
        write_file(result, '')


# Create a new file
def write_file(path, data):
    with open(path, 'w', encoding="utf-8") as f: # 'w' for write
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a', encoding="utf-8") as file: # 'a' for append
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    if  os.path.isfile(path):
        open(path, 'w', encoding="utf-8").close()


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt', encoding="utf-8") as f:
        for line in f:
            results.add(line.replace('\n', '')) # remove new line character
    return results


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name, "w", encoding="utf-8") as f: #added encoding for UnicodeEncodeError 
        for l in sorted(links):
            url = l.replace(" ","") # remove spaces
            f.write(l+"\n")
