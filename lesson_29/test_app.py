import unittest
from app import connect_to_db, create_table, insert_record, update_record, delete_record, select_records


class TestApp(unittest.TestCase):
    def setUp(self):
        self.conn = connect_to_db()
        create_table(self.conn)

    def tearDown(self):
        cur = self.conn.cursor()
        cur.execute("DROP TABLE IF EXISTS test_table")
        self.conn.commit()
        self.conn.close()

    def test_insert_and_select(self):
        insert_record(self.conn, "Test1")
        records = select_records(self.conn)
        self.assertGreater(len(records), 0)
        self.assertEqual(records[0][1], "Test1")

    def test_update(self):
        insert_record(self.conn, "Old")
        records = select_records(self.conn)
        id = records[0][0]
        update_record(self.conn, id, "New")
        records = select_records(self.conn)
        self.assertEqual(records[0][1], "New")

    def test_delete(self):
        insert_record(self.conn, "ToDelete")
        records = select_records(self.conn)
        id = records[0][0]
        delete_record(self.conn, id)
        records = select_records(self.conn)
        self.assertEqual(len(records), 0)

    def test_connection(self):
        self.assertIsNotNone(self.conn)


if __name__ == "__main__":
    unittest.main()