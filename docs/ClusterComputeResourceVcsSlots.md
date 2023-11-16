# ClusterComputeResourceVcsSlots


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | **str** | Identifier of the system for which the slots are applicable.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**datastore** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Datastores on the host which are recommended for vCLS VM deployment.  ***Since:*** vSphere API 7.0.3.0  Refers instances of *Datastore*.  | [optional] 
**total_slots** | **int** | The number of total vSphere Cluster Services slots on the host.  ***Since:*** vSphere API 7.0.1.1  | 

## Example

```python
from vmware_vi.models.cluster_compute_resource_vcs_slots import ClusterComputeResourceVcsSlots

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceVcsSlots from a JSON string
cluster_compute_resource_vcs_slots_instance = ClusterComputeResourceVcsSlots.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceVcsSlots.to_json()

# convert the object into a dict
cluster_compute_resource_vcs_slots_dict = cluster_compute_resource_vcs_slots_instance.to_dict()
# create an instance of ClusterComputeResourceVcsSlots from a dict
cluster_compute_resource_vcs_slots_form_dict = cluster_compute_resource_vcs_slots.from_dict(cluster_compute_resource_vcs_slots_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


