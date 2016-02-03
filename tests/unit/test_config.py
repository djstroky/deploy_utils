import ConfigParser
import os

from unittest import TestCase

from deploy_utils import CONFIG_DIR, TEMPLATE_DIR
from deploy_utils.config import DefaultConfig, ConfigHelper


class TestDefaultConfig(TestCase):

    def setUp(self):
        cp = ConfigParser.ConfigParser()
        cp.set('DEFAULT', 'test_key', 'test_value')
        self.default_conf = DefaultConfig(cp)

    def test_get(self):
        assert 'test_value' == self.default_conf.get('test_key')

    def test_make_params_for_template(self):
        out = self.default_conf.make_params_for_template(os.path.join(TEMPLATE_DIR, 'test_conf.ini'))
        assert 'test_key' in out
        assert out['test_key'] == 'test_value'
        assert 'chicharrones' in out
        assert out['chicharrones'] == None


class TestConfigHelper(TestCase):

    def setUp(self):
        self.conf_helper = ConfigHelper(CONFIG_DIR, TEMPLATE_DIR)

    def test_get_config(self):
        with open(os.path.join(CONFIG_DIR, 'test_temp.ini'), 'w') as f:
            f.write("[DEFAULT]\ntest_key = {test_key}")

        conf = self.conf_helper.get_config('test_temp')
        assert isinstance(conf, DefaultConfig)

    def test_setup(self):
        pass

    def test_write_template(self):
        pass
