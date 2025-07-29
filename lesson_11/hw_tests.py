import unittest
from hw10 import log_event

class HomeworkTests(unittest.TestCase):

    def test_log_event_success_positive(self):
        log_event("user1", "success")
        with open('login_system.log', 'r') as f:
            log_content = f.read()
        self.assertIn("Login event - Username: user1, Status: success", log_content)

    def test_log_event_expired_positive(self):
        log_event("user2", "expired")
        with open('login_system.log', 'r') as f:
            log_content = f.read()
        self.assertIn("Login event - Username: user2, Status: expired", log_content)

    def test_log_event_failed_positive(self):
        log_event("user3", "failed")
        with open('login_system.log', 'r') as f:
            log_content = f.read()
        self.assertIn("Login event - Username: user3, Status: failed", log_content)

    def test_log_event_long_username_positive(self):
        log_event("very_long_username_123", "success")
        with open('login_system.log', 'r') as f:
            log_content = f.read()
        self.assertIn("Login event - Username: very_long_username_123, Status: success", log_content)

    def test_log_event_very_short_username_positive(self):
        log_event("K", "success")
        with open('login_system.log', 'r') as f:
            log_content = f.read()
        self.assertIn("Login event - Username: K, Status: success", log_content)

    # Негативные тест кейсы
    def test_log_event_none_username_negative(self):
        with self.assertRaises(TypeError):
            log_event(None, "success")

    def test_log_event_none_status_negative(self):
        with self.assertRaises(TypeError):
            log_event("user4", None)

    def test_log_event_invalid_status_negative(self):
        with self.assertRaises(ValueError):
            log_event("user5", "invalid")

    def test_log_event_number_username_negative(self):
        with self.assertRaises(TypeError):
            log_event(123, "success")

    def test_log_event_number_status_negative(self):
        with self.assertRaises(TypeError):
            log_event("user6", 123)