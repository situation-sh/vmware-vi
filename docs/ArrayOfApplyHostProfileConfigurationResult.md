# ArrayOfApplyHostProfileConfigurationResult

A boxed array of *ApplyHostProfileConfigurationResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ApplyHostProfileConfigurationResult]**](ApplyHostProfileConfigurationResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_apply_host_profile_configuration_result import ArrayOfApplyHostProfileConfigurationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfApplyHostProfileConfigurationResult from a JSON string
array_of_apply_host_profile_configuration_result_instance = ArrayOfApplyHostProfileConfigurationResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfApplyHostProfileConfigurationResult.to_json()

# convert the object into a dict
array_of_apply_host_profile_configuration_result_dict = array_of_apply_host_profile_configuration_result_instance.to_dict()
# create an instance of ArrayOfApplyHostProfileConfigurationResult from a dict
array_of_apply_host_profile_configuration_result_form_dict = array_of_apply_host_profile_configuration_result.from_dict(array_of_apply_host_profile_configuration_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


