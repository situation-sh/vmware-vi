# ArrayOfHostProfileValidationFailureInfo

A boxed array of *HostProfileValidationFailureInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostProfileValidationFailureInfo]**](HostProfileValidationFailureInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_profile_validation_failure_info import ArrayOfHostProfileValidationFailureInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostProfileValidationFailureInfo from a JSON string
array_of_host_profile_validation_failure_info_instance = ArrayOfHostProfileValidationFailureInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostProfileValidationFailureInfo.to_json()

# convert the object into a dict
array_of_host_profile_validation_failure_info_dict = array_of_host_profile_validation_failure_info_instance.to_dict()
# create an instance of ArrayOfHostProfileValidationFailureInfo from a dict
array_of_host_profile_validation_failure_info_form_dict = array_of_host_profile_validation_failure_info.from_dict(array_of_host_profile_validation_failure_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


