# DVPortState

The state of a DistributedVirtualPort.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtime_info** | [**DVPortStatus**](DVPortStatus.md) |  | [optional] 
**stats** | [**DistributedVirtualSwitchPortStatistics**](DistributedVirtualSwitchPortStatistics.md) |  | 
**vendor_specific_state** | [**List[DistributedVirtualSwitchKeyedOpaqueBlob]**](DistributedVirtualSwitchKeyedOpaqueBlob.md) | Opaque binary blob that stores vendor-specific runtime state data.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.dv_port_state import DVPortState

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortState from a JSON string
dv_port_state_instance = DVPortState.from_json(json)
# print the JSON string representation of the object
print DVPortState.to_json()

# convert the object into a dict
dv_port_state_dict = dv_port_state_instance.to_dict()
# create an instance of DVPortState from a dict
dv_port_state_form_dict = dv_port_state.from_dict(dv_port_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


