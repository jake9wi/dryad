"""Genrate a DYRAD page."""


def gen_a_row():
    """Randomize a str of letters."""
    import secrets
    import string
    import locale
    locale.setlocale(locale.LC_ALL, 'C')

    alphabet = string.ascii_uppercase[0:-1]
    row = ''

    while len(alphabet) != 0:
        letter = secrets.choice(alphabet)
        row += letter
        alphabet = alphabet.replace(letter, '')

    return row


def fmt_a_row(row):
    """Add Spaces to the row."""
    sp = ' '
    row = row[0:4] + sp + row[4:7] + sp + \
        row[7:10] + sp + row[10:12] + sp + \
        row[12:14] + sp + row[14:17] + sp + \
        row[17:19] + sp + row[19:21] + sp + \
        row[21:23] + sp + row[23:25]
    return row

arow = gen_a_row()
print(arow)

print(
    fmt_a_row(arow)
)

"""
f = open('file.txt', 'w',  encoding='utf_8_sig')

f.close()
"""
