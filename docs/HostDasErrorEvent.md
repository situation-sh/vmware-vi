# HostDasErrorEvent

Deprecated as of vSphere API 5.0, the Server will generate the *EventEx* event with the *EventEx.eventTypeId* property set to \"com.vmware.vc.HA.HostAgentErrorEvent\".  This event records when there is a HA error on a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**reason** | **str** | The reason for the failure.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_das_error_event import HostDasErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostDasErrorEvent from a JSON string
host_das_error_event_instance = HostDasErrorEvent.from_json(json)
# print the JSON string representation of the object
print HostDasErrorEvent.to_json()

# convert the object into a dict
host_das_error_event_dict = host_das_error_event_instance.to_dict()
# create an instance of HostDasErrorEvent from a dict
host_das_error_event_form_dict = host_das_error_event.from_dict(host_das_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


