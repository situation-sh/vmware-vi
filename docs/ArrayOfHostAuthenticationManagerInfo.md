# ArrayOfHostAuthenticationManagerInfo

A boxed array of *HostAuthenticationManagerInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostAuthenticationManagerInfo]**](HostAuthenticationManagerInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_authentication_manager_info import ArrayOfHostAuthenticationManagerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostAuthenticationManagerInfo from a JSON string
array_of_host_authentication_manager_info_instance = ArrayOfHostAuthenticationManagerInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostAuthenticationManagerInfo.to_json()

# convert the object into a dict
array_of_host_authentication_manager_info_dict = array_of_host_authentication_manager_info_instance.to_dict()
# create an instance of ArrayOfHostAuthenticationManagerInfo from a dict
array_of_host_authentication_manager_info_form_dict = array_of_host_authentication_manager_info.from_dict(array_of_host_authentication_manager_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


