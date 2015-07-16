# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.

from unittest import TestCase
import main


class TestAPD(TestCase):
    def setUp(self):
        super(TestAPD, self).setUp()
        self.apd = main.APD()

    def tearDown(self):
        super(TestAPD, self).tearDown()

    def test_get_db_source_connection(self):
        expected_source_connection_data = dict(
            dailect="source dialiect",
            host="source_host",
            port="source_port",
            user="source_user",
            pw="source_pw",
            db_name="source_db_name")
        self.assertDictEqual(self.apd.get_db_source_connection(), 
                             expected_source_connection_data)

    def test_get_db_destination_connection(self):
        expected_destination_connection_data = dict(
            dailect="destination dialiect",
            host="destination_host",
            port="destination_port",
            user="destination_user",
            pw="destination_pw",
            db_name="destination_db_name")
        self.assertDictEqual(self.apd.get_db_source_connection(), 
                             expected_destination_connection_data)

    def test_run(self):
        self.assertIn(main.main(),
                      "ArPrData Application successfully started")
