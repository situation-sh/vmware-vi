# DatastoreCapacityIncreasedEvent

This event records when increase in a datastore's capacity is observed.  It may happen due to different reasons, like extending or expanding a datastore.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_capacity** | **int** | The old datastore capacity.  ***Since:*** vSphere API 4.0  | 
**new_capacity** | **int** | The new datastore capacity.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.datastore_capacity_increased_event import DatastoreCapacityIncreasedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreCapacityIncreasedEvent from a JSON string
datastore_capacity_increased_event_instance = DatastoreCapacityIncreasedEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreCapacityIncreasedEvent.to_json()

# convert the object into a dict
datastore_capacity_increased_event_dict = datastore_capacity_increased_event_instance.to_dict()
# create an instance of DatastoreCapacityIncreasedEvent from a dict
datastore_capacity_increased_event_form_dict = datastore_capacity_increased_event.from_dict(datastore_capacity_increased_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


