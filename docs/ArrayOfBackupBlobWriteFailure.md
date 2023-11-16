# ArrayOfBackupBlobWriteFailure

A boxed array of *BackupBlobWriteFailure*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[BackupBlobWriteFailure]**](BackupBlobWriteFailure.md) |  | 

## Example

```python
from vmware_vi.models.array_of_backup_blob_write_failure import ArrayOfBackupBlobWriteFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfBackupBlobWriteFailure from a JSON string
array_of_backup_blob_write_failure_instance = ArrayOfBackupBlobWriteFailure.from_json(json)
# print the JSON string representation of the object
print ArrayOfBackupBlobWriteFailure.to_json()

# convert the object into a dict
array_of_backup_blob_write_failure_dict = array_of_backup_blob_write_failure_instance.to_dict()
# create an instance of ArrayOfBackupBlobWriteFailure from a dict
array_of_backup_blob_write_failure_form_dict = array_of_backup_blob_write_failure.from_dict(array_of_backup_blob_write_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


