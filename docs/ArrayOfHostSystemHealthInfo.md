# ArrayOfHostSystemHealthInfo

A boxed array of *HostSystemHealthInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSystemHealthInfo]**](HostSystemHealthInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_system_health_info import ArrayOfHostSystemHealthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSystemHealthInfo from a JSON string
array_of_host_system_health_info_instance = ArrayOfHostSystemHealthInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSystemHealthInfo.to_json()

# convert the object into a dict
array_of_host_system_health_info_dict = array_of_host_system_health_info_instance.to_dict()
# create an instance of ArrayOfHostSystemHealthInfo from a dict
array_of_host_system_health_info_form_dict = array_of_host_system_health_info.from_dict(array_of_host_system_health_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


