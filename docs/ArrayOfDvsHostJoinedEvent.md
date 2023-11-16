# ArrayOfDvsHostJoinedEvent

A boxed array of *DvsHostJoinedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsHostJoinedEvent]**](DvsHostJoinedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_host_joined_event import ArrayOfDvsHostJoinedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsHostJoinedEvent from a JSON string
array_of_dvs_host_joined_event_instance = ArrayOfDvsHostJoinedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsHostJoinedEvent.to_json()

# convert the object into a dict
array_of_dvs_host_joined_event_dict = array_of_dvs_host_joined_event_instance.to_dict()
# create an instance of ArrayOfDvsHostJoinedEvent from a dict
array_of_dvs_host_joined_event_form_dict = array_of_dvs_host_joined_event.from_dict(array_of_dvs_host_joined_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


