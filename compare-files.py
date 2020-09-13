print("Compare Golden Config File vs. New Config\n")
with open('n.txt', 'r') as file1:
    with open('standard.txt', 'r') as file2:
        difference = set(file1).difference(file2)

difference.discard('\n')

with open('d.txt', 'w') as file_out:
    for line in difference:
        file_out.write("Difference in New Config: " + line)
        print("The New config has the following that the standard does not: \n")
        print("Difference in file: " + line)
