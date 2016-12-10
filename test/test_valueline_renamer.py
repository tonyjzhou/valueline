import unittest

from worker.valueline_renamer import extract_file_name


class ValuelineReaderTestCase(unittest.TestCase):
    def test_extract_file_name(self):
        self.assertEqual("NYSE-JNJ_JOHNSON&JOHNSON.pdf", extract_file_name('../resources/f4979.pdf'))

    def test_extract_file_name2(self):
        self.assertEqual("NYSE-VZ_VERIZON.pdf", extract_file_name('../resources/f1086.pdf'))

    def test_extract_file_name3(self):
        self.assertEqual("NYSE-CAT_CATERPILLARINC.pdf", extract_file_name('../resources/f1767.pdf'))

    def test_extract_file_name4(self):
        self.assertEqual("NDQ-CSCO_CISCOSYSTEMS.pdf", extract_file_name('../resources/f2009.pdf'))

    def test_extract_file_name5(self):
        self.assertEqual("TSE-BBDB.TOE_BOMBARDIERINC‚B™.pdf", extract_file_name('../resources/f1263.pdf'))

    def test_extract_file_name6(self):
        self.assertEqual("ASE-IAF_ABERDEENAUSEQ.pdf", extract_file_name('../resources/f3390.pdf'))

    def test_extract_file_name7(self):
        self.assertEqual("PNK-FUJIY_FUJIFILMHLDGS(ADR).pdf", extract_file_name('../resources/f3695.pdf'))

    def test_extract_file_name8(self):
        self.assertEqual("NYSE-PSX_PHILLIPS66.pdf", extract_file_name('../resources/f19788.pdf'))


if __name__ == '__main__':
    unittest.main()
