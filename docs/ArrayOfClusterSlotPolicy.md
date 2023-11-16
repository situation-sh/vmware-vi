# ArrayOfClusterSlotPolicy

A boxed array of *ClusterSlotPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterSlotPolicy]**](ClusterSlotPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_slot_policy import ArrayOfClusterSlotPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterSlotPolicy from a JSON string
array_of_cluster_slot_policy_instance = ArrayOfClusterSlotPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterSlotPolicy.to_json()

# convert the object into a dict
array_of_cluster_slot_policy_dict = array_of_cluster_slot_policy_instance.to_dict()
# create an instance of ArrayOfClusterSlotPolicy from a dict
array_of_cluster_slot_policy_form_dict = array_of_cluster_slot_policy.from_dict(array_of_cluster_slot_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

