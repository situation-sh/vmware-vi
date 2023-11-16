# ArrayOfClusterHostPowerAction

A boxed array of *ClusterHostPowerAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterHostPowerAction]**](ClusterHostPowerAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_host_power_action import ArrayOfClusterHostPowerAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterHostPowerAction from a JSON string
array_of_cluster_host_power_action_instance = ArrayOfClusterHostPowerAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterHostPowerAction.to_json()

# convert the object into a dict
array_of_cluster_host_power_action_dict = array_of_cluster_host_power_action_instance.to_dict()
# create an instance of ArrayOfClusterHostPowerAction from a dict
array_of_cluster_host_power_action_form_dict = array_of_cluster_host_power_action.from_dict(array_of_cluster_host_power_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


