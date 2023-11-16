# VirtualMachineFeatureRequirement

Feature requirement contains a key, featureName and an opaque value  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Accessor name to the feature requirement test  ***Since:*** vSphere API 5.1  | 
**feature_name** | **str** | Name of the feature.  Identical to the key.  ***Since:*** vSphere API 5.1  | 
**value** | **str** | Opaque value for the feature operation.  Operation is contained in the value.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.virtual_machine_feature_requirement import VirtualMachineFeatureRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFeatureRequirement from a JSON string
virtual_machine_feature_requirement_instance = VirtualMachineFeatureRequirement.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFeatureRequirement.to_json()

# convert the object into a dict
virtual_machine_feature_requirement_dict = virtual_machine_feature_requirement_instance.to_dict()
# create an instance of VirtualMachineFeatureRequirement from a dict
virtual_machine_feature_requirement_form_dict = virtual_machine_feature_requirement.from_dict(virtual_machine_feature_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


