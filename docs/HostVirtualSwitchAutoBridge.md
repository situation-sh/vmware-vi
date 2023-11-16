# HostVirtualSwitchAutoBridge

This data type describes a bridge that automatically selects a particular physical network adapter on the host according to some predetermined policy.  Used primarily to support mobility scenarios. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded_nic_device** | **List[str]** | List of physical network adapters that have been excluded from participating in the AutoBridge  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_switch_auto_bridge import HostVirtualSwitchAutoBridge

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualSwitchAutoBridge from a JSON string
host_virtual_switch_auto_bridge_instance = HostVirtualSwitchAutoBridge.from_json(json)
# print the JSON string representation of the object
print HostVirtualSwitchAutoBridge.to_json()

# convert the object into a dict
host_virtual_switch_auto_bridge_dict = host_virtual_switch_auto_bridge_instance.to_dict()
# create an instance of HostVirtualSwitchAutoBridge from a dict
host_virtual_switch_auto_bridge_form_dict = host_virtual_switch_auto_bridge.from_dict(host_virtual_switch_auto_bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


