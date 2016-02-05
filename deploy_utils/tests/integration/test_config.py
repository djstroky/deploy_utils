import ConfigParser
import os

from unittest import TestCase

import deploy_utils
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

        conf_file = os.path.join(CONFIG_DIR, 'test_temp.ini')
        with open(conf_file, 'w') as f:
            f.write("[DEFAULT]\ntest_key = {test_val}")

        conf = self.conf_helper.get_config('test_temp')
        assert isinstance(conf, DefaultConfig)
        assert '{test_key}' == conf.get('test_key')

        os.remove(conf_file)

    def test_setup(self):

        conf_file = os.path.join(CONFIG_DIR, 'test_temp.ini')
        try:
            os.remove(conf_file)
        except:
            pass

        deploy_utils.config.input = lambda _: 'blah'
        self.conf_helper.setup('test_temp')

        assert os.path.exists(conf_file)
        with open(conf_file) as f:
            contents = f.read()
            assert 'test_key=blah' in contents

        os.remove(conf_file)

    def test_write_template(self):

        conf_file = os.path.join(CONFIG_DIR, 'test_temp.ini')
        try:
            os.remove(conf_file)
        except:
            pass

        self.conf_helper.write_template(dict(test_key='blah blah'),
                                        os.path.join(TEMPLATE_DIR, 'test_temp'))

        assert os.path.exists(conf_file)
        with open(conf_file) as f:
            contents = f.read()
            assert 'test_key=blah blah' in contents

        os.remove(conf_file)
