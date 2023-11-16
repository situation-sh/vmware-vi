# VslmInfrastructureObjectPolicy

The data object type describes improved virtual disk infrastructure namespace storage policy details.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**backing_object_id** | **str** |  | 
**profile_id** | **str** |  | 
**error** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vslm_infrastructure_object_policy import VslmInfrastructureObjectPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of VslmInfrastructureObjectPolicy from a JSON string
vslm_infrastructure_object_policy_instance = VslmInfrastructureObjectPolicy.from_json(json)
# print the JSON string representation of the object
print VslmInfrastructureObjectPolicy.to_json()

# convert the object into a dict
vslm_infrastructure_object_policy_dict = vslm_infrastructure_object_policy_instance.to_dict()
# create an instance of VslmInfrastructureObjectPolicy from a dict
vslm_infrastructure_object_policy_form_dict = vslm_infrastructure_object_policy.from_dict(vslm_infrastructure_object_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


