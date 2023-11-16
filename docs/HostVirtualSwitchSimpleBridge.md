# HostVirtualSwitchSimpleBridge

A bridge that is statically bound to a single physical network adapter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nic_device** | **str** | The key of the physical network adapter to be bridged.  | 

## Example

```python
from vmware_vi.models.host_virtual_switch_simple_bridge import HostVirtualSwitchSimpleBridge

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualSwitchSimpleBridge from a JSON string
host_virtual_switch_simple_bridge_instance = HostVirtualSwitchSimpleBridge.from_json(json)
# print the JSON string representation of the object
print HostVirtualSwitchSimpleBridge.to_json()

# convert the object into a dict
host_virtual_switch_simple_bridge_dict = host_virtual_switch_simple_bridge_instance.to_dict()
# create an instance of HostVirtualSwitchSimpleBridge from a dict
host_virtual_switch_simple_bridge_form_dict = host_virtual_switch_simple_bridge.from_dict(host_virtual_switch_simple_bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


