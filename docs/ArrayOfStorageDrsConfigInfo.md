# ArrayOfStorageDrsConfigInfo

A boxed array of *StorageDrsConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageDrsConfigInfo]**](StorageDrsConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_drs_config_info import ArrayOfStorageDrsConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageDrsConfigInfo from a JSON string
array_of_storage_drs_config_info_instance = ArrayOfStorageDrsConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageDrsConfigInfo.to_json()

# convert the object into a dict
array_of_storage_drs_config_info_dict = array_of_storage_drs_config_info_instance.to_dict()
# create an instance of ArrayOfStorageDrsConfigInfo from a dict
array_of_storage_drs_config_info_form_dict = array_of_storage_drs_config_info.from_dict(array_of_storage_drs_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


