# ArrayOfDvsCreatedEvent

A boxed array of *DvsCreatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsCreatedEvent]**](DvsCreatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_created_event import ArrayOfDvsCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsCreatedEvent from a JSON string
array_of_dvs_created_event_instance = ArrayOfDvsCreatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsCreatedEvent.to_json()

# convert the object into a dict
array_of_dvs_created_event_dict = array_of_dvs_created_event_instance.to_dict()
# create an instance of ArrayOfDvsCreatedEvent from a dict
array_of_dvs_created_event_form_dict = array_of_dvs_created_event.from_dict(array_of_dvs_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


