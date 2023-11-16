# ArrayOfStorageIORMConfigOption

A boxed array of *StorageIORMConfigOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageIORMConfigOption]**](StorageIORMConfigOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_iorm_config_option import ArrayOfStorageIORMConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageIORMConfigOption from a JSON string
array_of_storage_iorm_config_option_instance = ArrayOfStorageIORMConfigOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageIORMConfigOption.to_json()

# convert the object into a dict
array_of_storage_iorm_config_option_dict = array_of_storage_iorm_config_option_instance.to_dict()
# create an instance of ArrayOfStorageIORMConfigOption from a dict
array_of_storage_iorm_config_option_form_dict = array_of_storage_iorm_config_option.from_dict(array_of_storage_iorm_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


