# DuplicateIpDetectedEvent

This event records that a duplicate IP address has been observed in conflict with the vmotion or IP storage interface configured on the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duplicate_ip** | **str** | The Duplicate IP address detected.  ***Since:*** VI API 2.5  | 
**mac_address** | **str** | The MAC associated with duplicate IP.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.duplicate_ip_detected_event import DuplicateIpDetectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateIpDetectedEvent from a JSON string
duplicate_ip_detected_event_instance = DuplicateIpDetectedEvent.from_json(json)
# print the JSON string representation of the object
print DuplicateIpDetectedEvent.to_json()

# convert the object into a dict
duplicate_ip_detected_event_dict = duplicate_ip_detected_event_instance.to_dict()
# create an instance of DuplicateIpDetectedEvent from a dict
duplicate_ip_detected_event_form_dict = duplicate_ip_detected_event.from_dict(duplicate_ip_detected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


