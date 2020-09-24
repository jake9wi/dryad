"""Genrate a DYRAD page."""
import locale
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--begin', type=str, dest='begin', default='990000 ABC 99')
parser.add_argument('--end', type=str, dest='end', default='992359 ABC 99')
args = parser.parse_args()

locale.setlocale(locale.LC_ALL, 'C')

def gen_a_row():
    """Randomize a str of letters."""
    import secrets
    import string

    alphabet = string.ascii_uppercase[0:-1]
    row = ''

    while len(alphabet) != 0:
        letter = secrets.choice(alphabet)
        row += letter
        alphabet = alphabet.replace(letter, '')

    return row


def row_dict(row):
    """Split row into cells."""
    row = {
        'c0': row[0:4],
        'c1': row[4:7],
        'c2': row[7:10],
        'c3': row[10:12],
        'c4': row[12:14],
        'c5': row[14:17],
        'c6': row[17:19],
        'c7': row[19:21],
        'c8': row[21:23],
        'c9': row[23:25],
    }
    return row

DryadRows = 'ABCDEFGHIJKLMNOPQRSTUVWXY'

BcstRows = list(range(1,9)) + list(range(11,19))

DryadDict = {}
BcstDict = {}

for row in DryadRows:
    DryadDict[row] = row_dict(gen_a_row())

for row in BcstRows:
    BcstDict[row] = gen_a_row()

f = open('dryad.html', 'w',  encoding='utf_8_sig')
print("<html><head>", file=f)
print("<style>", file=f)
print("body { font-family: monospace; }", file=f)
print("td { padding-right: 8pt; }", file=f)
print(".cent { text-align: center; }", file=f)
print(".bold { font-weight: bold; }", file=f)
print("</style>", file=f)
print("</head><body>", file=f) 

print("<p><b>Valid:</b> {} <b>/</b> {}</p>".format(
    args.begin, args.end), file=f)
print("<hr/>", file=f)

print("<p><b>DRYAD Cipher Sheet</b></p>", file=f)

print("<table><tbody>", file=f)

for key, row in DryadDict.items():
    if key in 'AGMS':
        print("<tr>", file=f)
        print("<td></td>", file=f)
        print("<td class=\"bold\"> ABC</td>", file=f)
        print("<td class=\"bold\">DEF</td>", file=f)
        print("<td class=\"bold\">GHJ</td>", file=f)
        print("<td class=\"bold\">KL</td>", file=f)
        print("<td class=\"bold\">MN</td>", file=f)
        print("<td class=\"bold\">PQR</td>", file=f)
        print("<td class=\"bold\">ST</td>", file=f)
        print("<td class=\"bold\">UV</td>", file=f)
        print("<td class=\"bold\">WX</td>", file=f)
        print("<td class=\"bold\">YZ</td>", file=f)
        print("</tr>", file=f)

        print("<tr>", file=f)
        print("<td></td>", file=f)
        print("<td class=\"cent bold\">0</td>", file=f)
        print("<td class=\"cent bold\">1</td>", file=f)
        print("<td class=\"cent bold\">2</td>", file=f)
        print("<td class=\"cent bold\">3</td>", file=f)
        print("<td class=\"cent bold\">4</td>", file=f)
        print("<td class=\"cent bold\">5</td>", file=f)
        print("<td class=\"cent bold\">6</td>", file=f)
        print("<td class=\"cent bold\">7</td>", file=f)
        print("<td class=\"cent bold\">8</td>", file=f)
        print("<td class=\"cent bold\">9</td>", file=f)
        print("</tr>", file=f)

    print("<tr>", file=f)
    print("<td class=\"bold\"> {}</td>".format(key), file=f)
    for cell in row.values():
        print("<td>{}</td>".format(cell), file=f)
    print("</tr>", file=f)

print("</tbody></table>", file=f)
print("<hr/>", file=f)
print("<p><b>Broadcast Authorizations</b></p>", file=f)

print("<table><tbody>", file=f)
print("<tr>", file=f)
print("<td>{}</td>".format(BcstDict[1][:4]), file=f)
print("<td>{}</td>".format(BcstDict[2][:4]), file=f)
print("<td>{}</td>".format(BcstDict[3][:4]), file=f)
print("<td>{}</td>".format(BcstDict[4][:4]), file=f)
print("<td>{}</td>".format(BcstDict[5][:4]), file=f)
print("<td>{}</td>".format(BcstDict[6][:4]), file=f)
print("<td>{}</td>".format(BcstDict[7][:4]), file=f)
print("<td>{}</td>".format(BcstDict[8][:4]), file=f)
print("</tr>", file=f)
print("<tr>", file=f)
print("<td>{}</td>".format(BcstDict[11][:4]), file=f)
print("<td>{}</td>".format(BcstDict[12][:4]), file=f)
print("<td>{}</td>".format(BcstDict[13][:4]), file=f)
print("<td>{}</td>".format(BcstDict[14][:4]), file=f)
print("<td>{}</td>".format(BcstDict[15][:4]), file=f)
print("<td>{}</td>".format(BcstDict[16][:4]), file=f)
print("<td>{}</td>".format(BcstDict[17][:4]), file=f)
print("<td>{}</td>".format(BcstDict[18][:4]), file=f)
print("</tr>", file=f)
print("</tbody></table>", file=f)
print("</body></html>", file=f)
f.close()
