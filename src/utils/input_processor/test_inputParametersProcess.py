import json
import os
import unittest

import paramtasks


class TestInputParametersProcess(unittest.TestCase):

    def test_input_param_init(self):
        unittest.TestCase.assertTrue(self, self.input_param_obj.framework == 'test_framework')

    def setUp(self):
        data = {"framework": "test_framework"
            , "model": "test_model",
                "source_image": {
                    "source_image_folder": "test_source_image_folder",
                    "source_image_search_string": "",
                    "source_image_augment": "True"
                },
                "output_upload": {
                    "upload_location": "",
                    "cred_user": "",
                    "cred_password": ""
                },
                "training_infra": {
                    "ssh_path": "",
                    "hostname": ""
                }
                }

        with open('./temp_test.json', 'w') as outfile:
            json.dump(data, outfile)
        self.input_param_obj = paramtasks.InputParametersProcess('./temp_test.json')

    def tearDown(self):
        self.input_param_obj = None
        os.remove('./temp_test.json')


if __name__ == '__main__':
    unittest.main()
