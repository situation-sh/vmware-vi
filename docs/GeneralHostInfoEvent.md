# GeneralHostInfoEvent

This event is the general information event for a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.general_host_info_event import GeneralHostInfoEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralHostInfoEvent from a JSON string
general_host_info_event_instance = GeneralHostInfoEvent.from_json(json)
# print the JSON string representation of the object
print GeneralHostInfoEvent.to_json()

# convert the object into a dict
general_host_info_event_dict = general_host_info_event_instance.to_dict()
# create an instance of GeneralHostInfoEvent from a dict
general_host_info_event_form_dict = general_host_info_event.from_dict(general_host_info_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


