# ClusterSlotPolicy

The base class *ClusterSlotPolicy* is used for specifying how the slot size is to be computed for the failover level HA admission control policy.  By default, vSphere HA defines the slot size using the largest memory and cpu reservations of any powered on virtual machine in the cluster. Subclasses of this class define various policies to modify how the slot size is chosen to prevent outlier virtual machines (i.e. those with much larger reservations than the average) from skewing the slot size. If such a policy is chosen, outlier virtual machines will use multiple slots. Using such a policy introduces a risk that vSphere HA will be unable to failover these virtual machines because of resource fragmentation.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cluster_slot_policy import ClusterSlotPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSlotPolicy from a JSON string
cluster_slot_policy_instance = ClusterSlotPolicy.from_json(json)
# print the JSON string representation of the object
print ClusterSlotPolicy.to_json()

# convert the object into a dict
cluster_slot_policy_dict = cluster_slot_policy_instance.to_dict()
# create an instance of ClusterSlotPolicy from a dict
cluster_slot_policy_form_dict = cluster_slot_policy.from_dict(cluster_slot_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


