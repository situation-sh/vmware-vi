# DvsPortUnblockedEvent

A port is unblocked in the distributed virtual switch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_key** | **str** | The port key.  ***Since:*** vSphere API 4.0  | 
**runtime_info** | [**DVPortStatus**](DVPortStatus.md) |  | [optional] 
**prev_block_state** | **str** | Previous state of the DvsPort.  See *DvsEventPortBlockState_enum*  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.dvs_port_unblocked_event import DvsPortUnblockedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsPortUnblockedEvent from a JSON string
dvs_port_unblocked_event_instance = DvsPortUnblockedEvent.from_json(json)
# print the JSON string representation of the object
print DvsPortUnblockedEvent.to_json()

# convert the object into a dict
dvs_port_unblocked_event_dict = dvs_port_unblocked_event_instance.to_dict()
# create an instance of DvsPortUnblockedEvent from a dict
dvs_port_unblocked_event_form_dict = dvs_port_unblocked_event.from_dict(dvs_port_unblocked_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


