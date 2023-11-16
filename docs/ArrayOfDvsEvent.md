# ArrayOfDvsEvent

A boxed array of *DvsEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsEvent]**](DvsEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_event import ArrayOfDvsEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsEvent from a JSON string
array_of_dvs_event_instance = ArrayOfDvsEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsEvent.to_json()

# convert the object into a dict
array_of_dvs_event_dict = array_of_dvs_event_instance.to_dict()
# create an instance of ArrayOfDvsEvent from a dict
array_of_dvs_event_form_dict = array_of_dvs_event.from_dict(array_of_dvs_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


