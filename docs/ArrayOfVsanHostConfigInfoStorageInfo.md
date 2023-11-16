# ArrayOfVsanHostConfigInfoStorageInfo

A boxed array of *VsanHostConfigInfoStorageInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostConfigInfoStorageInfo]**](VsanHostConfigInfoStorageInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_config_info_storage_info import ArrayOfVsanHostConfigInfoStorageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostConfigInfoStorageInfo from a JSON string
array_of_vsan_host_config_info_storage_info_instance = ArrayOfVsanHostConfigInfoStorageInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostConfigInfoStorageInfo.to_json()

# convert the object into a dict
array_of_vsan_host_config_info_storage_info_dict = array_of_vsan_host_config_info_storage_info_instance.to_dict()
# create an instance of ArrayOfVsanHostConfigInfoStorageInfo from a dict
array_of_vsan_host_config_info_storage_info_form_dict = array_of_vsan_host_config_info_storage_info.from_dict(array_of_vsan_host_config_info_storage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


