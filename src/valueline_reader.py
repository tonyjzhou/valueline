#!/usr/bin/env python3
import glob
import re

import PyPDF2


def extract_file_name(pdf_name):
    with open(pdf_name, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        page = pdf_reader.getPage(0)
        content = page.extractText().replace('\n', '')

        print(content)

        result = search_result(content)

        company_name = result.group(1).replace('.', '')
        company_symbol = result.group(2)

        return "%s_%s.pdf" % (company_symbol, company_name)


def search_result(content):
    exchanges = ['NYSE', 'NDQ', 'TSE', 'ASE', 'PNK']

    for e in exchanges:
        p = re.compile('.*\d+(\D+)(%s-\D+).*' % e)
        result = p.search(content)
        if result:
            return result


def main():
    # print(extract_file_name('../resources/f3695.pdf'))
    for file_name in glob.glob("/Users/tonyzhou/Google Drive/Investment/Valueline/stk1700/*.pdf"):
        print(file_name)
        print(extract_file_name(file_name))
        print()


if __name__ == "__main__":
    main()
