# DvsEvent

These are dvs-related events.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_event import DvsEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsEvent from a JSON string
dvs_event_instance = DvsEvent.from_json(json)
# print the JSON string representation of the object
print DvsEvent.to_json()

# convert the object into a dict
dvs_event_dict = dvs_event_instance.to_dict()
# create an instance of DvsEvent from a dict
dvs_event_form_dict = dvs_event.from_dict(dvs_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


