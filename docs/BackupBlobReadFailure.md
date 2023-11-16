# BackupBlobReadFailure

Thrown if backupConfig blob is corrupted  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_name** | **str** | The entity name on which backupConfig read failed  ***Since:*** vSphere API 5.1  | 
**entity_type** | **str** | The entity type on which backupConfig read failed  ***Since:*** vSphere API 5.1  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.backup_blob_read_failure import BackupBlobReadFailure

# TODO update the JSON string below
json = "{}"
# create an instance of BackupBlobReadFailure from a JSON string
backup_blob_read_failure_instance = BackupBlobReadFailure.from_json(json)
# print the JSON string representation of the object
print BackupBlobReadFailure.to_json()

# convert the object into a dict
backup_blob_read_failure_dict = backup_blob_read_failure_instance.to_dict()
# create an instance of BackupBlobReadFailure from a dict
backup_blob_read_failure_form_dict = backup_blob_read_failure.from_dict(backup_blob_read_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


