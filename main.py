def word_count(input_file, output_file):
        with open(input_file, 'r') as file:
            lines = file.readlines()
        wc = {}
        for line in lines:
            words = line.strip().split()
            for word in words:
                if word in wc:
                    wc[word] += 1
                else:
                    wc[word] = 1
        with open(output_file, 'w') as file:
            for line in lines:
                file.write(line)
            file.write("\nWord_Count:\n")
            for word, count in wc.items():
                file.write(f"{word}: {count}\n")

input_file = "input.txt"
output_file = "output.txt"

word_count(input_file, output_file)


