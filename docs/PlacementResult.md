# PlacementResult

*ClusterComputeResource.PlaceVm* method can invoke DRS for recommendations for target hosts and datastores for placing a virtual machine and its virtual disks using xVMotion.  PlacementResult is the class of the result returned by that method.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**List[ClusterRecommendation]**](ClusterRecommendation.md) | The list of recommendations for where to place the virtual machine and its virtual disks.  ***Since:*** vSphere API 6.0  | [optional] 
**drs_fault** | [**ClusterDrsFaults**](ClusterDrsFaults.md) |  | [optional] 

## Example

```python
from vmware_vi.models.placement_result import PlacementResult

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementResult from a JSON string
placement_result_instance = PlacementResult.from_json(json)
# print the JSON string representation of the object
print PlacementResult.to_json()

# convert the object into a dict
placement_result_dict = placement_result_instance.to_dict()
# create an instance of PlacementResult from a dict
placement_result_form_dict = placement_result.from_dict(placement_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


