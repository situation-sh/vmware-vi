# ClusterFixedSizeSlotPolicy

This policy allows setting a fixed slot size  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** | The cpu component of the slot size (in MHz)  ***Since:*** vSphere API 5.1  | 
**memory** | **int** | The memory component of the slot size (in megabytes)  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.cluster_fixed_size_slot_policy import ClusterFixedSizeSlotPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFixedSizeSlotPolicy from a JSON string
cluster_fixed_size_slot_policy_instance = ClusterFixedSizeSlotPolicy.from_json(json)
# print the JSON string representation of the object
print ClusterFixedSizeSlotPolicy.to_json()

# convert the object into a dict
cluster_fixed_size_slot_policy_dict = cluster_fixed_size_slot_policy_instance.to_dict()
# create an instance of ClusterFixedSizeSlotPolicy from a dict
cluster_fixed_size_slot_policy_form_dict = cluster_fixed_size_slot_policy.from_dict(cluster_fixed_size_slot_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


