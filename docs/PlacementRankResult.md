# PlacementRankResult

PlacementRankResult is the class of the result returned by the vCenter Server for rankClustersForPlacement method  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Reference key for the placement request  ***Since:*** vSphere API 6.0  | 
**candidate** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**reserved_space_mb** | **int** | The reserved storage space for the candidate cluster after placement The unit is in Megabytes  ***Since:*** vSphere API 6.0  | 
**used_space_mb** | **int** | The expected space usage for the candidate cluster after placement The unit is in Megabytes  ***Since:*** vSphere API 6.0  | 
**total_space_mb** | **int** | The expected total space for the candidate cluster after placement The unit is in Megabytes  ***Since:*** vSphere API 6.0  | 
**utilization** | **float** | The expected aggregate resource utilization for the candidate cluster after placement The unit is a fractional value between 0 and 1.  ***Since:*** vSphere API 6.0  | 
**faults** | [**List[MethodFault]**](MethodFault.md) | Information about why a given cluster is not recommended for placement  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.placement_rank_result import PlacementRankResult

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementRankResult from a JSON string
placement_rank_result_instance = PlacementRankResult.from_json(json)
# print the JSON string representation of the object
print PlacementRankResult.to_json()

# convert the object into a dict
placement_rank_result_dict = placement_rank_result_instance.to_dict()
# create an instance of PlacementRankResult from a dict
placement_rank_result_form_dict = placement_rank_result.from_dict(placement_rank_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


