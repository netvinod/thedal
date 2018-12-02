import json

'''
This deals with reading and validating params.

'''


class InputParametersProcess:
    def __init__(self, input_param_file):
        data = json.load(open(input_param_file))

        self.framework = data['framework']
        self.model = data['model']
        self.source_image_folder = data['source_image']['source_image_folder']
        self.source_image_search_string = data['source_image']['source_image_search_string']
        self.source_image_augment = data['source_image']['source_image_augment']
        self.output_upload_location = data['output_upload']['upload_location']
        self.output_cred_user = data['output_upload']['cred_user']
        self.output_cred_password = data['output_upload']['cred_password']
        self.training_hostname = data['training_infra']['hostname']
        self.training_ssh_path = data['training_infra']['ssh_path']
