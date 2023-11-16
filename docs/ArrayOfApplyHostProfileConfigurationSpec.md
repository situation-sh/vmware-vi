# ArrayOfApplyHostProfileConfigurationSpec

A boxed array of *ApplyHostProfileConfigurationSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ApplyHostProfileConfigurationSpec]**](ApplyHostProfileConfigurationSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_apply_host_profile_configuration_spec import ArrayOfApplyHostProfileConfigurationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfApplyHostProfileConfigurationSpec from a JSON string
array_of_apply_host_profile_configuration_spec_instance = ArrayOfApplyHostProfileConfigurationSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfApplyHostProfileConfigurationSpec.to_json()

# convert the object into a dict
array_of_apply_host_profile_configuration_spec_dict = array_of_apply_host_profile_configuration_spec_instance.to_dict()
# create an instance of ArrayOfApplyHostProfileConfigurationSpec from a dict
array_of_apply_host_profile_configuration_spec_form_dict = array_of_apply_host_profile_configuration_spec.from_dict(array_of_apply_host_profile_configuration_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


