# HostVirtualSwitchConfig

This data object type describes the VirtualSwitch configuration containing both the configurable properties on a VirtualSwitch and identification information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_operation** | **str** | This property indicates the change operation to apply on this configuration specification.  See also *HostConfigChangeOperation_enum*.  | [optional] 
**name** | **str** | The name of the virtual switch.  Maximum length is 32 characters.  | 
**spec** | [**HostVirtualSwitchSpec**](HostVirtualSwitchSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_switch_config import HostVirtualSwitchConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualSwitchConfig from a JSON string
host_virtual_switch_config_instance = HostVirtualSwitchConfig.from_json(json)
# print the JSON string representation of the object
print HostVirtualSwitchConfig.to_json()

# convert the object into a dict
host_virtual_switch_config_dict = host_virtual_switch_config_instance.to_dict()
# create an instance of HostVirtualSwitchConfig from a dict
host_virtual_switch_config_form_dict = host_virtual_switch_config.from_dict(host_virtual_switch_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


