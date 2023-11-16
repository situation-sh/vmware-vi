# VsanPolicySatisfiability

PolicySatisfiablity -- Structure to describe whether a policy can be satisfied.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the object.  ***Since:*** vSphere API 5.5  | [optional] 
**is_satisfiable** | **bool** | Can the policy be satisfied given the assumptions of the API that queried satisfiability.  See also *HostVsanInternalSystem.ReconfigurationSatisfiable*.  ***Since:*** vSphere API 5.5  | 
**reason** | [**LocalizableMessage**](LocalizableMessage.md) |  | [optional] 
**cost** | [**VsanPolicyCost**](VsanPolicyCost.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vsan_policy_satisfiability import VsanPolicySatisfiability

# TODO update the JSON string below
json = "{}"
# create an instance of VsanPolicySatisfiability from a JSON string
vsan_policy_satisfiability_instance = VsanPolicySatisfiability.from_json(json)
# print the JSON string representation of the object
print VsanPolicySatisfiability.to_json()

# convert the object into a dict
vsan_policy_satisfiability_dict = vsan_policy_satisfiability_instance.to_dict()
# create an instance of VsanPolicySatisfiability from a dict
vsan_policy_satisfiability_form_dict = vsan_policy_satisfiability.from_dict(vsan_policy_satisfiability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


