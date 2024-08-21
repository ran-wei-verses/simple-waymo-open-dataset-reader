import pickle
import tensorflow as tf
from simple_waymo_open_dataset_reader import scenario_pb2
from simple_waymo_open_dataset_reader import motion_utils

FILENAME = '../data/uncompressed_scenario_training_training.tfrecord-00000-of-01000'
dataset = tf.data.TFRecordDataset(FILENAME, compression_type="")
data = next(iter(dataset))

# parse scenario protobuf
scenario = scenario_pb2.Scenario()
scenario.ParseFromString(bytes(data.numpy()))

# convert protobuf to json
scenario_dict = motion_utils.waymo_to_scenario(scenario)

print(scenario_dict)

with open("../data/parsed_data.p", "wb") as f:
    pickle.dump(scenario_dict, f)