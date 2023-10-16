from os import walk

files_by_ext = {}
for _, _, files in walk("."):
    for file in files:
        extension = file.split(".")[-1]
        files_by_ext.setdefault(extension, []).append(file)

with open("report.txt", "w") as output:
    for ext, files in sorted(files_by_ext.items()):
        output.write(f".{ext}\n")
        for file in sorted(files):
            output.write(f"- - - {file}\n")
