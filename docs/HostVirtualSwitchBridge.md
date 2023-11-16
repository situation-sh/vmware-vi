# HostVirtualSwitchBridge

A bridge connects a virtual switch to a physical network adapter.  There are multiple types of bridges. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_virtual_switch_bridge import HostVirtualSwitchBridge

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualSwitchBridge from a JSON string
host_virtual_switch_bridge_instance = HostVirtualSwitchBridge.from_json(json)
# print the JSON string representation of the object
print HostVirtualSwitchBridge.to_json()

# convert the object into a dict
host_virtual_switch_bridge_dict = host_virtual_switch_bridge_instance.to_dict()
# create an instance of HostVirtualSwitchBridge from a dict
host_virtual_switch_bridge_form_dict = host_virtual_switch_bridge.from_dict(host_virtual_switch_bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


