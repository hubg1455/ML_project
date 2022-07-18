from collections import namedtuple

DataIngestionArtifact=namedtuple("DataIngestionArtifact",["train_path","test_path","is_ingested","message"])

DataValidationArtifact = namedtuple("DataValidationArtifact",
["schema_file_path","report_file_path","report_page_file_path","is_validated","message"])