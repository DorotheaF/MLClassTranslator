lang = "russian"
short = "ru"
general_path = "C:\\Users\\Dorot\\OneDrive\\College\\Graduate\\Classes\\Machine_Learning\\MLClassTranslator\\Data\\"

second_lang_file = general_path + lang + "\\opus.en-" + short + "-train." + short
english_file = general_path + lang + "\\opus.en-" + short + "-train.en"
dest_file = general_path + lang + "\\"
farsi_path = general_path + "farsi\\farsi_bible.txt"

mixed = []

with open(second_lang_file, encoding="UTF8") as reader:
    lines = reader.readlines()
    mixed = mixed + lines[0:8000]
    print(len(lines))

with open(dest_file + "train_parent.trg", "w", encoding="UTF8") as writer:
    lines_to_write = lines[0:int(len(lines)*(9/10))]
    writer.writelines(lines_to_write)

with open(dest_file + "dev_parent.trg", "w", encoding="UTF8") as writer:
    lines_to_write = lines[int(len(lines) * (9 / 10)):int(len(lines))]
    writer.writelines(lines_to_write)

with open(english_file, encoding="UTF8") as reader:
    lines = reader.readlines()
    mixed = mixed + lines[0:8000]

with open(dest_file + "train_parent.src", "w", encoding="UTF8") as writer:
    lines_to_write = lines[0:int(len(lines) * (9 / 10))]
    writer.writelines(lines_to_write)

with open(dest_file + "dev_parent.src", "w", encoding="UTF8") as writer:
    lines_to_write = lines[int(len(lines) * (9 / 10)):int(len(lines))]
    writer.writelines(lines_to_write)

with open(farsi_path, encoding="UTF8") as reader:
    lines = reader.readlines()
    mixed = mixed + lines

with open(dest_file + "mixed.txt", "w", encoding="UTF8") as writer:
    print(len(mixed))
    writer.writelines(mixed)
