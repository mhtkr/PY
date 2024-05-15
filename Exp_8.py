#Experiment - 8

with open('input.txt', 'r') as input_file:
    data = input_file.read()

processed_data = data.upper()


with open('output.txt', 'w') as output_file:
    output_file.write(processed_data)
