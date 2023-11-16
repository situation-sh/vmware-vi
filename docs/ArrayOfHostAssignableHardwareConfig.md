# ArrayOfHostAssignableHardwareConfig

A boxed array of *HostAssignableHardwareConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostAssignableHardwareConfig]**](HostAssignableHardwareConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_assignable_hardware_config import ArrayOfHostAssignableHardwareConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostAssignableHardwareConfig from a JSON string
array_of_host_assignable_hardware_config_instance = ArrayOfHostAssignableHardwareConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostAssignableHardwareConfig.to_json()

# convert the object into a dict
array_of_host_assignable_hardware_config_dict = array_of_host_assignable_hardware_config_instance.to_dict()
# create an instance of ArrayOfHostAssignableHardwareConfig from a dict
array_of_host_assignable_hardware_config_form_dict = array_of_host_assignable_hardware_config.from_dict(array_of_host_assignable_hardware_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


