# ArrayOfHostVirtualSwitchConfig

A boxed array of *HostVirtualSwitchConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVirtualSwitchConfig]**](HostVirtualSwitchConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_virtual_switch_config import ArrayOfHostVirtualSwitchConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVirtualSwitchConfig from a JSON string
array_of_host_virtual_switch_config_instance = ArrayOfHostVirtualSwitchConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVirtualSwitchConfig.to_json()

# convert the object into a dict
array_of_host_virtual_switch_config_dict = array_of_host_virtual_switch_config_instance.to_dict()
# create an instance of ArrayOfHostVirtualSwitchConfig from a dict
array_of_host_virtual_switch_config_form_dict = array_of_host_virtual_switch_config.from_dict(array_of_host_virtual_switch_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


