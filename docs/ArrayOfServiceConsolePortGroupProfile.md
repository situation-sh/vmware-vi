# ArrayOfServiceConsolePortGroupProfile

A boxed array of *ServiceConsolePortGroupProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ServiceConsolePortGroupProfile]**](ServiceConsolePortGroupProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_service_console_port_group_profile import ArrayOfServiceConsolePortGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfServiceConsolePortGroupProfile from a JSON string
array_of_service_console_port_group_profile_instance = ArrayOfServiceConsolePortGroupProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfServiceConsolePortGroupProfile.to_json()

# convert the object into a dict
array_of_service_console_port_group_profile_dict = array_of_service_console_port_group_profile_instance.to_dict()
# create an instance of ArrayOfServiceConsolePortGroupProfile from a dict
array_of_service_console_port_group_profile_form_dict = array_of_service_console_port_group_profile.from_dict(array_of_service_console_port_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


