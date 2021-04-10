"""Genrate a DYRAD page."""
import locale
import argparse
import secrets
import string
import typing as ty

parser = argparse.ArgumentParser()

parser.add_argument('--begin', type=str, dest='begin',
                    default='990000 ABC 99',
                    help='The DTG of begin of valid period.')

parser.add_argument('--end', type=str, dest='end',
                    default='992359 ABC 99',
                    help='The DTG of end of valid period.')

args = parser.parse_args()

locale.setlocale(locale.LC_ALL, 'C')


def gen_row() -> str:
    """Randomize a str of letters."""
    alphabet = string.ascii_uppercase[0:-1]
    row_list = list()

    while len(alphabet) != 0:
        letter = secrets.choice(alphabet)
        row_list.append(letter)
        alphabet = alphabet.replace(letter, '')

    return ''.join(row_list)


def make_dryad_tuple() -> tuple:
    """Make 25 unique rows."""
    row_set: ty.Set[str] = set()
    while len(row_set) < 26:
        row_set.add(gen_row())

    dryad_list = list()

    while len(row_set) != 0:
        a_row = row_set.pop()

        row_dict = {
            'c0': a_row[0:4],
            'c1': a_row[4:7],
            'c2': a_row[7:10],
            'c3': a_row[10:12],
            'c4': a_row[12:14],
            'c5': a_row[14:17],
            'c6': a_row[17:19],
            'c7': a_row[19:21],
            'c8': a_row[21:23],
            'c9': a_row[23:25],
        }

        dryad_list.append(row_dict)

    return tuple(dryad_list)


def make_bcst_tuple() -> tuple:
    """Make 16 unique rows of 4 lettres."""
    row_set: ty.Set[str] = set()
    while len(row_set) < 17:
        a_row = gen_row()
        row_set.add(a_row[:4])

    return tuple(row_set)


dryad_keys = list(string.ascii_uppercase[0:-1])
dryad_tuple = make_dryad_tuple()

bcst_tuple = make_bcst_tuple()

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

for row in zip(dryad_keys, dryad_tuple):
    if row[0] in 'AGMS':
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
    print("<td class=\"bold\"> {}</td>".format(row[0]), file=f)
    for cell in row[1].values():
        print("<td>{}</td>".format(cell), file=f)
    print("</tr>", file=f)

print("</tbody></table>", file=f)
print("<hr/>", file=f)
print("<p><b>Broadcast Authorizations</b></p>", file=f)

print("<table><tbody>", file=f)
print("<tr>", file=f)
print("<td>{}</td>".format(bcst_tuple[1]), file=f)
print("<td>{}</td>".format(bcst_tuple[2]), file=f)
print("<td>{}</td>".format(bcst_tuple[3]), file=f)
print("<td>{}</td>".format(bcst_tuple[4]), file=f)
print("<td>{}</td>".format(bcst_tuple[5]), file=f)
print("<td>{}</td>".format(bcst_tuple[6]), file=f)
print("<td>{}</td>".format(bcst_tuple[7]), file=f)
print("<td>{}</td>".format(bcst_tuple[8]), file=f)
print("</tr>", file=f)
print("<tr>", file=f)
print("<td>{}</td>".format(bcst_tuple[9]), file=f)
print("<td>{}</td>".format(bcst_tuple[10]), file=f)
print("<td>{}</td>".format(bcst_tuple[11]), file=f)
print("<td>{}</td>".format(bcst_tuple[12]), file=f)
print("<td>{}</td>".format(bcst_tuple[13]), file=f)
print("<td>{}</td>".format(bcst_tuple[14]), file=f)
print("<td>{}</td>".format(bcst_tuple[15]), file=f)
print("<td>{}</td>".format(bcst_tuple[15]), file=f)
print("</tr>", file=f)
print("</tbody></table>", file=f)
print("</body></html>", file=f)
f.close()
