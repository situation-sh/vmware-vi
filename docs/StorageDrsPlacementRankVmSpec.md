# StorageDrsPlacementRankVmSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_placement_spec** | [**PlacementSpec**](PlacementSpec.md) |  | 
**vm_clusters** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Set of candidate clusters for the placement request  ***Since:*** vSphere API 6.0  Refers instances of *ClusterComputeResource*.  | 

## Example

```python
from vmware_vi.models.storage_drs_placement_rank_vm_spec import StorageDrsPlacementRankVmSpec

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsPlacementRankVmSpec from a JSON string
storage_drs_placement_rank_vm_spec_instance = StorageDrsPlacementRankVmSpec.from_json(json)
# print the JSON string representation of the object
print StorageDrsPlacementRankVmSpec.to_json()

# convert the object into a dict
storage_drs_placement_rank_vm_spec_dict = storage_drs_placement_rank_vm_spec_instance.to_dict()
# create an instance of StorageDrsPlacementRankVmSpec from a dict
storage_drs_placement_rank_vm_spec_form_dict = storage_drs_placement_rank_vm_spec.from_dict(storage_drs_placement_rank_vm_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


