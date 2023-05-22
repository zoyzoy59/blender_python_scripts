import os

# Get the list of .py files in the repository
file_list = [file for file in os.listdir() if file.endswith(".py")]

# Read the existing content of the README.md file
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()

# Add the file names to the README content
file_names = "\n".join(file_list)
updated_content = f"{readme_content}\n\n## Python Scripts\n\n{file_names}"

# Write the updated content back to the README.md file
with open("README.md", "w") as readme_file:
    readme_file.write(updated_content)
