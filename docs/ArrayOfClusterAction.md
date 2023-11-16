# ArrayOfClusterAction

A boxed array of *ClusterAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterAction]**](ClusterAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_action import ArrayOfClusterAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterAction from a JSON string
array_of_cluster_action_instance = ArrayOfClusterAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterAction.to_json()

# convert the object into a dict
array_of_cluster_action_dict = array_of_cluster_action_instance.to_dict()
# create an instance of ArrayOfClusterAction from a dict
array_of_cluster_action_form_dict = array_of_cluster_action.from_dict(array_of_cluster_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


