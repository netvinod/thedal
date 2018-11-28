import keras
import tensorflow as tf 
import tarfile
import sys
import os
import wget



'''Deals with Tensorflow model'''

def run_training(self, **kwargs):
    '''
    This function recieves the following params and runs the training
    It returns back trained model path.
    Params:

    base_model_url - Urls of the base model path
    input_images_folder -Input images path
    bounding_box_label_path - Path of the file containing the mapping between
                              bounding box and images
    return
    model_path                   
    '''
    pass
def _save_to_model(self, **kwargs):
    pass
def _download_model(model_directory, download_url):
    '''
    Downloads the model and extracts the chkpoint from a pre-trained model

    Params:
    base_model_urls
    return
    Extracted path
    '''

    filename = wget.download(download_url,os.path.join(model_directory,filename))
    return os.path.join(model_directory,filename)
def _prepare_config_file_for_training(self, **kwargs):
    pass
def _extract_model(file_path, extracted_folder):

    tarfile.open(filepath, 'r:gz').extractall(dest_directory)
def _upload_model(self, **kwargs):
    pass
