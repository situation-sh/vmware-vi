# ClusterActionHistory

Base class for all action history.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ClusterAction**](ClusterAction.md) |  | 
**time** | **datetime** | The time when the action was executed.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.cluster_action_history import ClusterActionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterActionHistory from a JSON string
cluster_action_history_instance = ClusterActionHistory.from_json(json)
# print the JSON string representation of the object
print ClusterActionHistory.to_json()

# convert the object into a dict
cluster_action_history_dict = cluster_action_history_instance.to_dict()
# create an instance of ClusterActionHistory from a dict
cluster_action_history_form_dict = cluster_action_history.from_dict(cluster_action_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


