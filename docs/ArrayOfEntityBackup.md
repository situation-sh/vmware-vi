# ArrayOfEntityBackup

A boxed array of *EntityBackup*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EntityBackup]**](EntityBackup.md) |  | 

## Example

```python
from vmware_vi.models.array_of_entity_backup import ArrayOfEntityBackup

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEntityBackup from a JSON string
array_of_entity_backup_instance = ArrayOfEntityBackup.from_json(json)
# print the JSON string representation of the object
print ArrayOfEntityBackup.to_json()

# convert the object into a dict
array_of_entity_backup_dict = array_of_entity_backup_instance.to_dict()
# create an instance of ArrayOfEntityBackup from a dict
array_of_entity_backup_form_dict = array_of_entity_backup.from_dict(array_of_entity_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


