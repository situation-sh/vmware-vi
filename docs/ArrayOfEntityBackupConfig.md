# ArrayOfEntityBackupConfig

A boxed array of *EntityBackupConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EntityBackupConfig]**](EntityBackupConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_entity_backup_config import ArrayOfEntityBackupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEntityBackupConfig from a JSON string
array_of_entity_backup_config_instance = ArrayOfEntityBackupConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfEntityBackupConfig.to_json()

# convert the object into a dict
array_of_entity_backup_config_dict = array_of_entity_backup_config_instance.to_dict()
# create an instance of ArrayOfEntityBackupConfig from a dict
array_of_entity_backup_config_form_dict = array_of_entity_backup_config.from_dict(array_of_entity_backup_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


