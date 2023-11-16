# VslmInfrastructureObjectPolicySpec

Specification to assign a SPBM policy to FCD infrastructure object (namespace).  This is used in object-based storage.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | SPBM Profile to associate.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.vslm_infrastructure_object_policy_spec import VslmInfrastructureObjectPolicySpec

# TODO update the JSON string below
json = "{}"
# create an instance of VslmInfrastructureObjectPolicySpec from a JSON string
vslm_infrastructure_object_policy_spec_instance = VslmInfrastructureObjectPolicySpec.from_json(json)
# print the JSON string representation of the object
print VslmInfrastructureObjectPolicySpec.to_json()

# convert the object into a dict
vslm_infrastructure_object_policy_spec_dict = vslm_infrastructure_object_policy_spec_instance.to_dict()
# create an instance of VslmInfrastructureObjectPolicySpec from a dict
vslm_infrastructure_object_policy_spec_form_dict = vslm_infrastructure_object_policy_spec.from_dict(vslm_infrastructure_object_policy_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


