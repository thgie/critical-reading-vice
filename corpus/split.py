import os
import re

def search_and_copy_files(folder_path, regex_pattern):
    # Create a regex pattern object
    pattern = re.compile(regex_pattern)

    # Iterate over files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file
        if os.path.isfile(file_path):

            print(file_path)
            with open(file_path, 'r') as file:
                content = file.read()

            # Search for matches using the regex pattern
            matches = re.findall(pattern, content)

            # If there are matches, create a new file and copy the matching content
            if matches:

                print(f"Matches found in {filename}.")

                new_filename = f"{filename}"
                comment_file_path = os.path.join('comments/', new_filename)
                code_file_path = os.path.join('code/', new_filename)

                with open(comment_file_path, 'w') as new_file:

                    # Write the matching content to the new file and remove license
                    comments = re.sub(r" \*? {1,2}This [VICE|file|library|program][\s\S]*(USA|licenses\/>)\.?", '', '\n'.join(matches))
                    new_file.write(comments)

                with open(code_file_path, 'w') as new_file:
                    new_file.write(re.sub(regex_pattern, '', content))

folder_path = 'src/'
regex_pattern = re.compile(r'/\*(.*?)\*/', re.DOTALL)
search_and_copy_files(folder_path, regex_pattern)
