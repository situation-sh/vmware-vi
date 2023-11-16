# IncorrectHostInformationEvent

This event records if the host did not provide the information needed to acquire the correct set of licenses.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.incorrect_host_information_event import IncorrectHostInformationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of IncorrectHostInformationEvent from a JSON string
incorrect_host_information_event_instance = IncorrectHostInformationEvent.from_json(json)
# print the JSON string representation of the object
print IncorrectHostInformationEvent.to_json()

# convert the object into a dict
incorrect_host_information_event_dict = incorrect_host_information_event_instance.to_dict()
# create an instance of IncorrectHostInformationEvent from a dict
incorrect_host_information_event_form_dict = incorrect_host_information_event.from_dict(incorrect_host_information_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


