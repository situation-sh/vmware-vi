# PlacementRankSpec

PlacementRankSpec encapsulates all of the inputs passed to the *StorageResourceManager.RankForPlacement* method.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specs** | [**List[PlacementSpec]**](PlacementSpec.md) | List of VM placement specifications for ranking clusters  ***Since:*** vSphere API 6.0  | 
**clusters** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of candidate clusters for the placement request  ***Since:*** vSphere API 6.0  Refers instances of *ClusterComputeResource*.  | 
**rules** | [**List[PlacementAffinityRule]**](PlacementAffinityRule.md) | List of affinity rules for the placement request  ***Since:*** vSphere API 6.0  | [optional] 
**placement_rank_by_vm** | [**List[StorageDrsPlacementRankVmSpec]**](StorageDrsPlacementRankVmSpec.md) | List of preferred clusters for individual VM placement requests  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.placement_rank_spec import PlacementRankSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementRankSpec from a JSON string
placement_rank_spec_instance = PlacementRankSpec.from_json(json)
# print the JSON string representation of the object
print PlacementRankSpec.to_json()

# convert the object into a dict
placement_rank_spec_dict = placement_rank_spec_instance.to_dict()
# create an instance of PlacementRankSpec from a dict
placement_rank_spec_form_dict = placement_rank_spec.from_dict(placement_rank_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


