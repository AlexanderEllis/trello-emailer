from send_email import send_email
import unittest

class EmailerTest(unittest.TestCase):
    """
    Testing the script's functionality
    """

    def test_email_functionality(self):
        """
        This function tests the send_email function
        """
        self.assertTrue(send_email('This is a test message.'))
