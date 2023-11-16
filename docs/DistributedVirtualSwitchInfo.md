# DistributedVirtualSwitchInfo

This class describes a DistributedVirtualSwitch that a device backing can attached to its ports.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_name** | **str** | The name of the switch.  ***Since:*** vSphere API 4.0  | 
**switch_uuid** | **str** | The UUID of the switch.  ***Since:*** vSphere API 4.0  | 
**distributed_virtual_switch** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**network_reservation_supported** | **bool** | Indicates whether network bandwidth reservation is supported on the switch  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_info import DistributedVirtualSwitchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchInfo from a JSON string
distributed_virtual_switch_info_instance = DistributedVirtualSwitchInfo.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchInfo.to_json()

# convert the object into a dict
distributed_virtual_switch_info_dict = distributed_virtual_switch_info_instance.to_dict()
# create an instance of DistributedVirtualSwitchInfo from a dict
distributed_virtual_switch_info_form_dict = distributed_virtual_switch_info.from_dict(distributed_virtual_switch_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


