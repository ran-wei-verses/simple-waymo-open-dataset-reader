# Simple Waymo Open Motion Dataset Reader

This is a simple file reader for the [Waymo Open Dataset](https://waymo.com/open/) modified from the [simple-waymo-open-dataset-reader](https://github.com/gdlg/simple-waymo-open-dataset-reader). The main goal is to start interacting with the dataset quickly without installing the [waymo-open-dataset](https://github.com/waymo-research/waymo-open-dataset) repo, which doesn't work for Mac. It does not aim to replace the Waymo repo, especially the evaluation metrics that they provide.

We additionally borrowed some preprocessing code from [SceneInformer](https://github.com/sisl/SceneInformer) to convert motion dataset protobuf into a dictionary. 

## Installation
For dependencies, you only need `protobuf, tensorflow`:
```
pip install protobuf, tensorflow
```

Then install the repo:
```
pip install -e .
```

Optinally regenerate the `*_pb2.py` files from the protos:
```
sh generate_proto.sh
```

## Usage
To parse a motion dataset example, download `uncompressed/scenario/training/training.tfrecord-00000-of-01000` from thw Waymo website and then save it in a `./data` folder. Then run:
```
cd examples
python parse_motion_dataset.py
```
You should see a new file `parsed_data.p` in the `./data` folder.

**Google could storage setup**: You can download data directly from GCS without manually downloading the tfrecords. To set it up, first download the CLI package from [here](https://cloud.google.com/sdk/docs/install-sdk) and go through items a, b, and c. Then follow the TF dataset authentication instructions [here](https://www.tensorflow.org/datasets/gcs). 

To run the above example using GCS:
```
cd examples
python parse_motion_dataset.py --gcs True
```

## License

This code is released under the Apache License, version 2.0. This projects incorporate some parts of the [Waymo Open Dataset code](https://github.com/waymo-research/waymo-open-dataset/blob/master/README.md) (the files `simple_waymo_open_dataset_reader/*.proto`) and is licensed to you under their original license terms. See `LICENSE` file for details.

