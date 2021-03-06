#!/usr/bin/env python2

import unittest

from appscale.common import appscale_info
from appscale.datastore import dbconstants
from cassandra.cluster import Cluster
from appscale.datastore.cassandra_env import schema
from flexmock import flexmock


class TestCassandraPrimer(unittest.TestCase):
  def test_define_ua_schema(self):
    session = flexmock(execute=lambda statement, values: None)
    schema.define_ua_schema(session)

  def test_prime_cassandra(self):
    self.assertRaises(TypeError, schema.prime_cassandra, '1')
    self.assertRaises(
        dbconstants.AppScaleBadArg, schema.prime_cassandra, 0)

    flexmock(appscale_info).should_receive('get_db_ips').\
      and_return(['127.0.0.1'])

    session = flexmock(execute=lambda: None, set_keyspace=lambda: None)
    flexmock(Cluster).should_receive('connect').and_return(session)
    flexmock(schema).should_receive('define_ua_schema')
