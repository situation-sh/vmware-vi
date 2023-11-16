# HostDasEvent

Top-level event for host DAS events to extend.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_das_event import HostDasEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostDasEvent from a JSON string
host_das_event_instance = HostDasEvent.from_json(json)
# print the JSON string representation of the object
print HostDasEvent.to_json()

# convert the object into a dict
host_das_event_dict = host_das_event_instance.to_dict()
# create an instance of HostDasEvent from a dict
host_das_event_form_dict = host_das_event.from_dict(host_das_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


