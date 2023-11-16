# ClusterAction

Base class for all action recommendations in VirtualCenter.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the action.  This is encoded to differentiate between different types of actions aimed at achieving different goals.  ***Since:*** VI API 2.5  | 
**target** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_action import ClusterAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAction from a JSON string
cluster_action_instance = ClusterAction.from_json(json)
# print the JSON string representation of the object
print ClusterAction.to_json()

# convert the object into a dict
cluster_action_dict = cluster_action_instance.to_dict()
# create an instance of ClusterAction from a dict
cluster_action_form_dict = cluster_action.from_dict(cluster_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


