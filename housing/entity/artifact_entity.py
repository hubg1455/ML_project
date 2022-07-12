from collections import namedtuple

DataIngestionArtifact=namedtuple("DataIngestionArtifact",["train_path","test_path","is_ingested","message"])