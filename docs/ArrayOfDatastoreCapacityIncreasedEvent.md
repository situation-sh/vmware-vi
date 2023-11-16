# ArrayOfDatastoreCapacityIncreasedEvent

A boxed array of *DatastoreCapacityIncreasedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreCapacityIncreasedEvent]**](DatastoreCapacityIncreasedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_capacity_increased_event import ArrayOfDatastoreCapacityIncreasedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreCapacityIncreasedEvent from a JSON string
array_of_datastore_capacity_increased_event_instance = ArrayOfDatastoreCapacityIncreasedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreCapacityIncreasedEvent.to_json()

# convert the object into a dict
array_of_datastore_capacity_increased_event_dict = array_of_datastore_capacity_increased_event_instance.to_dict()
# create an instance of ArrayOfDatastoreCapacityIncreasedEvent from a dict
array_of_datastore_capacity_increased_event_form_dict = array_of_datastore_capacity_increased_event.from_dict(array_of_datastore_capacity_increased_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


