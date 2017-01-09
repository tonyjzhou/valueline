#!/usr/bin/env python3
import glob
import multiprocessing
import os
import re
from multiprocessing.pool import Pool

import PyPDF2


def extract_file_name(pdf_name):
    with open(pdf_name, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        page = pdf_reader.getPage(0)
        content = page.extractText().replace('\n', '')

        # print(content)

        result = search_result(content)

        path = os.path.dirname(os.path.abspath(pdf_name))
        company_name = result.group(1).replace('.', '').replace('/', '-')
        company_symbol = result.group(2)

        return "%s/%s_%s.pdf" % (path, company_symbol, company_name)


def search_result(content):
    exchanges = ['NDQ', 'NYSE', 'TSE', 'ASE', 'PNK']

    for e in exchanges:
        p = re.compile('^.*\d+(\D+.*)(%s-\D+).*' % e)
        result = p.search(content)
        if result:
            return result


def main():
    # print(extract_file_name('../resource/f19788.pdf'))
    # for file_name in glob.glob("/Users/tonyzhou/Google Drive/Investment/Valueline/stk1700-4/*.pdf"):
    #     print(file_name)
    #     rename_file(file_name)
    pool_size = multiprocessing.cpu_count() * 2
    Pool(pool_size).map(rename_file, glob.glob("/Users/tonyzhou/Google Drive/Investment/Valueline/stk1700-4/*.pdf"))


def rename_file(file_name):
    new_file_name = extract_file_name(file_name)
    print("Renaming '%s' to '%s'" % (file_name, new_file_name))
    os.rename(file_name, new_file_name)
    print()


if __name__ == "__main__":
    main()
