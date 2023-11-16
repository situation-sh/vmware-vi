# FeatureRequirementsNotMet

The host does not meet feature requirements of the virtual machine.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_requirement** | [**List[VirtualMachineFeatureRequirement]**](VirtualMachineFeatureRequirement.md) | The feature requirements that were not met.  ***Since:*** vSphere API 5.1  | [optional] 
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.feature_requirements_not_met import FeatureRequirementsNotMet

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureRequirementsNotMet from a JSON string
feature_requirements_not_met_instance = FeatureRequirementsNotMet.from_json(json)
# print the JSON string representation of the object
print FeatureRequirementsNotMet.to_json()

# convert the object into a dict
feature_requirements_not_met_dict = feature_requirements_not_met_instance.to_dict()
# create an instance of FeatureRequirementsNotMet from a dict
feature_requirements_not_met_form_dict = feature_requirements_not_met.from_dict(feature_requirements_not_met_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


