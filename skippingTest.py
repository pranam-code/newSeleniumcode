import unittest


class apptesting(unittest.TestCase):
    @unittest.SkipTest  # skip this test
    def test_search(self):
        print("this is search test")

    @unittest.skip("I am skipping this test bcz its not ready")
    def test_advancesearch(self):
        print("this is advance search test")

    @unittest.skipIf(1 == 1, "numbers are not equal")
    def test_prepaid(self):
        print("this is prepaid test")

    def test_postpaid(self):
        print("this is postpaid test")

    def test_loginbygmail(self):
        print("this is gmail login test")

    def test_loginbytwitter(self):
        print("this is twitter login test")


if __name__ == "__main__":
    unittest.main()
