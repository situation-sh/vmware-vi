# ArrayOfHostFlagInfo

A boxed array of *HostFlagInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFlagInfo]**](HostFlagInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_flag_info import ArrayOfHostFlagInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFlagInfo from a JSON string
array_of_host_flag_info_instance = ArrayOfHostFlagInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFlagInfo.to_json()

# convert the object into a dict
array_of_host_flag_info_dict = array_of_host_flag_info_instance.to_dict()
# create an instance of ArrayOfHostFlagInfo from a dict
array_of_host_flag_info_form_dict = array_of_host_flag_info.from_dict(array_of_host_flag_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


