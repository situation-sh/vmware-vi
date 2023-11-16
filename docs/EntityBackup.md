# EntityBackup

*EntityBackup* is an abstract data object that contains the related entity backup and restore elements for virtual distributed switches and virtual distributed portgroups.  See the following elements: - *EntityBackupConfig* - *EntityImportType_enum* - *EntityType_enum*    ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.entity_backup import EntityBackup

# TODO update the JSON string below
json = "{}"
# create an instance of EntityBackup from a JSON string
entity_backup_instance = EntityBackup.from_json(json)
# print the JSON string representation of the object
print EntityBackup.to_json()

# convert the object into a dict
entity_backup_dict = entity_backup_instance.to_dict()
# create an instance of EntityBackup from a dict
entity_backup_form_dict = entity_backup.from_dict(entity_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


