data_text = 'sdfdsgdfh dfghdf hgdfghfgh fghgfh fgh zfghfgh fghfg hgfhf fghfghfghfhfgh'
data_text = data_text.split()
max_len = len(max(data_text, key=len))

for i, item in enumerate(sorted(data_text), 1):
    print(f'{i}. {item:>{max_len}}')
    