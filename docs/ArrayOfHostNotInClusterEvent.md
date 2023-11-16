# ArrayOfHostNotInClusterEvent

A boxed array of *HostNotInClusterEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNotInClusterEvent]**](HostNotInClusterEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_not_in_cluster_event import ArrayOfHostNotInClusterEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNotInClusterEvent from a JSON string
array_of_host_not_in_cluster_event_instance = ArrayOfHostNotInClusterEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNotInClusterEvent.to_json()

# convert the object into a dict
array_of_host_not_in_cluster_event_dict = array_of_host_not_in_cluster_event_instance.to_dict()
# create an instance of ArrayOfHostNotInClusterEvent from a dict
array_of_host_not_in_cluster_event_form_dict = array_of_host_not_in_cluster_event.from_dict(array_of_host_not_in_cluster_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


