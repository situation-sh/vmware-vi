# ArrayOfDasClusterIsolatedEvent

A boxed array of *DasClusterIsolatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DasClusterIsolatedEvent]**](DasClusterIsolatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_das_cluster_isolated_event import ArrayOfDasClusterIsolatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDasClusterIsolatedEvent from a JSON string
array_of_das_cluster_isolated_event_instance = ArrayOfDasClusterIsolatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDasClusterIsolatedEvent.to_json()

# convert the object into a dict
array_of_das_cluster_isolated_event_dict = array_of_das_cluster_isolated_event_instance.to_dict()
# create an instance of ArrayOfDasClusterIsolatedEvent from a dict
array_of_das_cluster_isolated_event_form_dict = array_of_das_cluster_isolated_event.from_dict(array_of_das_cluster_isolated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


