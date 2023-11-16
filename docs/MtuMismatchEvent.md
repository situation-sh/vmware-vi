# MtuMismatchEvent

The value of MTU configured in the vSphere Distributed Switch mismatches physical switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.mtu_mismatch_event import MtuMismatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MtuMismatchEvent from a JSON string
mtu_mismatch_event_instance = MtuMismatchEvent.from_json(json)
# print the JSON string representation of the object
print MtuMismatchEvent.to_json()

# convert the object into a dict
mtu_mismatch_event_dict = mtu_mismatch_event_instance.to_dict()
# create an instance of MtuMismatchEvent from a dict
mtu_mismatch_event_form_dict = mtu_mismatch_event.from_dict(mtu_mismatch_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


