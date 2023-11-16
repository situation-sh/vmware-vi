# RecoveryEvent

This event is generated when recovery takes place on a management vmknic  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The host on which recovery happened  ***Since:*** vSphere API 5.1  | 
**port_key** | **str** | The key of the new port  ***Since:*** vSphere API 5.1  | 
**dvs_uuid** | **str** | The uuid of the DVS  ***Since:*** vSphere API 5.1  | [optional] 
**vnic** | **str** | The virtual management NIC device where recovery was done  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.recovery_event import RecoveryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveryEvent from a JSON string
recovery_event_instance = RecoveryEvent.from_json(json)
# print the JSON string representation of the object
print RecoveryEvent.to_json()

# convert the object into a dict
recovery_event_dict = recovery_event_instance.to_dict()
# create an instance of RecoveryEvent from a dict
recovery_event_form_dict = recovery_event.from_dict(recovery_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


