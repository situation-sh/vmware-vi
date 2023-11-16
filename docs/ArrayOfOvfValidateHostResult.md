# ArrayOfOvfValidateHostResult

A boxed array of *OvfValidateHostResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfValidateHostResult]**](OvfValidateHostResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_validate_host_result import ArrayOfOvfValidateHostResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfValidateHostResult from a JSON string
array_of_ovf_validate_host_result_instance = ArrayOfOvfValidateHostResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfValidateHostResult.to_json()

# convert the object into a dict
array_of_ovf_validate_host_result_dict = array_of_ovf_validate_host_result_instance.to_dict()
# create an instance of ArrayOfOvfValidateHostResult from a dict
array_of_ovf_validate_host_result_form_dict = array_of_ovf_validate_host_result.from_dict(array_of_ovf_validate_host_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


