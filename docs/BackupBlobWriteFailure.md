# BackupBlobWriteFailure

Thrown if backupConfig blob write fails  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_name** | **str** | The entity name on which backupConfig write failed  ***Since:*** vSphere API 5.1  | 
**entity_type** | **str** | The entity type on which backupConfig write failed  ***Since:*** vSphere API 5.1  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.backup_blob_write_failure import BackupBlobWriteFailure

# TODO update the JSON string below
json = "{}"
# create an instance of BackupBlobWriteFailure from a JSON string
backup_blob_write_failure_instance = BackupBlobWriteFailure.from_json(json)
# print the JSON string representation of the object
print BackupBlobWriteFailure.to_json()

# convert the object into a dict
backup_blob_write_failure_dict = backup_blob_write_failure_instance.to_dict()
# create an instance of BackupBlobWriteFailure from a dict
backup_blob_write_failure_form_dict = backup_blob_write_failure.from_dict(backup_blob_write_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


