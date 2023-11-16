# NoGuestHeartbeat

A powered-on virtual machine has a guest OS with Tools installed, but it does not have a valid heartbeat. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_guest_heartbeat import NoGuestHeartbeat

# TODO update the JSON string below
json = "{}"
# create an instance of NoGuestHeartbeat from a JSON string
no_guest_heartbeat_instance = NoGuestHeartbeat.from_json(json)
# print the JSON string representation of the object
print NoGuestHeartbeat.to_json()

# convert the object into a dict
no_guest_heartbeat_dict = no_guest_heartbeat_instance.to_dict()
# create an instance of NoGuestHeartbeat from a dict
no_guest_heartbeat_form_dict = no_guest_heartbeat.from_dict(no_guest_heartbeat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


