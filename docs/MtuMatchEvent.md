# MtuMatchEvent

The value of MTU configured in the vSphere Distributed Switch matches physical switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.mtu_match_event import MtuMatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MtuMatchEvent from a JSON string
mtu_match_event_instance = MtuMatchEvent.from_json(json)
# print the JSON string representation of the object
print MtuMatchEvent.to_json()

# convert the object into a dict
mtu_match_event_dict = mtu_match_event_instance.to_dict()
# create an instance of MtuMatchEvent from a dict
mtu_match_event_form_dict = mtu_match_event.from_dict(mtu_match_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


