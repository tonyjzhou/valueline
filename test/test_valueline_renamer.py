import unittest

from worker.valueline_renamer import extract_file_name


class ValuelineReaderTestCase(unittest.TestCase):
    def test_extract_file_name(self):
        self.assertTrue("NYSE-JNJ_JOHNSON&JOHNSON.pdf" in extract_file_name('../resource/f4979.pdf'))

    def test_extract_file_name2(self):
        self.assertTrue("NYSE-VZ_VERIZON.pdf" in extract_file_name('../resource/f1086.pdf'))

    def test_extract_file_name3(self):
        self.assertTrue("NYSE-CAT_CATERPILLARINC.pdf" in extract_file_name('../resource/f1767.pdf'))

    def test_extract_file_name4(self):
        self.assertTrue("NDQ-CSCO_CISCOSYSTEMS.pdf" in extract_file_name('../resource/f2009.pdf'))

    def test_extract_file_name5(self):
        self.assertTrue("TSE-BBDB.TOE_BOMBARDIERINC‚B™.pdf" in extract_file_name('../resource/f1263.pdf'))

    def test_extract_file_name6(self):
        self.assertTrue("ASE-IAF_ABERDEENAUSEQ.pdf" in extract_file_name('../resource/f3390.pdf'))

    def test_extract_file_name7(self):
        self.assertTrue("PNK-FUJIY_FUJIFILMHLDGS(ADR).pdf" in extract_file_name('../resource/f3695.pdf'))

    def test_extract_file_name8(self):
        self.assertTrue("NYSE-PSX_PHILLIPS66.pdf" in extract_file_name('../resource/f19788.pdf'))


if __name__ == '__main__':
    unittest.main()
