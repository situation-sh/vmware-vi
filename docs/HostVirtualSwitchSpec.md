# HostVirtualSwitchSpec

This data object type describes the VirtualSwitch specification representing the properties on a VirtualSwitch that can be configured once the object exists. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_ports** | **int** | The number of ports that this virtual switch is configured to use.  Changing this setting does not take effect until the next reboot. The maximum value is 1024, although other constraints, such as memory limits, may establish a lower effective limit.  | 
**bridge** | [**HostVirtualSwitchBridge**](HostVirtualSwitchBridge.md) |  | [optional] 
**policy** | [**HostNetworkPolicy**](HostNetworkPolicy.md) |  | [optional] 
**mtu** | **int** | The maximum transmission unit (MTU) of the virtual switch in bytes.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_switch_spec import HostVirtualSwitchSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualSwitchSpec from a JSON string
host_virtual_switch_spec_instance = HostVirtualSwitchSpec.from_json(json)
# print the JSON string representation of the object
print HostVirtualSwitchSpec.to_json()

# convert the object into a dict
host_virtual_switch_spec_dict = host_virtual_switch_spec_instance.to_dict()
# create an instance of HostVirtualSwitchSpec from a dict
host_virtual_switch_spec_form_dict = host_virtual_switch_spec.from_dict(host_virtual_switch_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


