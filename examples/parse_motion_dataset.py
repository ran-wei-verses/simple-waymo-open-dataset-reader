import argparse
import os
import pickle
import tensorflow as tf
from simple_waymo_open_dataset_reader import scenario_pb2
from simple_waymo_open_dataset_reader import motion_utils

true_str = lambda x: True if x.lower() == "true" else False
parser = argparse.ArgumentParser()
parser.add_argument("--gcs", type=true_str, default=False, help="Whether to get data from google cloud storage")
args = vars(parser.parse_args())

if args["gcs"]:
    print("getting dataset from gcs")
    FILENAME = 'gs://waymo_open_dataset_motion_v_1_2_1/uncompressed/scenario/training/training.tfrecord-00001-of-01000'
else:
    print("getting dataset from local")
    FILENAME = '../data/uncompressed_scenario_training_training.tfrecord-00000-of-01000'

dataset = tf.data.TFRecordDataset(FILENAME, compression_type="")
data = next(iter(dataset))

# parse scenario protobuf
scenario = scenario_pb2.Scenario()
scenario.ParseFromString(bytes(data.numpy()))

# convert protobuf to json
scenario_dict = motion_utils.waymo_to_scenario(scenario)

print(scenario_dict)

if not os.path.exists("../data"):
    os.makedirs("../data")
with open("../data/parsed_data.p", "wb") as f:
    pickle.dump(scenario_dict, f)

print("parsed data saved to ../data/parsed_data.p")