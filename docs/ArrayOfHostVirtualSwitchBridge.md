# ArrayOfHostVirtualSwitchBridge

A boxed array of *HostVirtualSwitchBridge*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVirtualSwitchBridge]**](HostVirtualSwitchBridge.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_virtual_switch_bridge import ArrayOfHostVirtualSwitchBridge

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVirtualSwitchBridge from a JSON string
array_of_host_virtual_switch_bridge_instance = ArrayOfHostVirtualSwitchBridge.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVirtualSwitchBridge.to_json()

# convert the object into a dict
array_of_host_virtual_switch_bridge_dict = array_of_host_virtual_switch_bridge_instance.to_dict()
# create an instance of ArrayOfHostVirtualSwitchBridge from a dict
array_of_host_virtual_switch_bridge_form_dict = array_of_host_virtual_switch_bridge.from_dict(array_of_host_virtual_switch_bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


