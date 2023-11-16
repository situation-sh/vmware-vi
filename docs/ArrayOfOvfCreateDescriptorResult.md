# ArrayOfOvfCreateDescriptorResult

A boxed array of *OvfCreateDescriptorResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfCreateDescriptorResult]**](OvfCreateDescriptorResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_create_descriptor_result import ArrayOfOvfCreateDescriptorResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfCreateDescriptorResult from a JSON string
array_of_ovf_create_descriptor_result_instance = ArrayOfOvfCreateDescriptorResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfCreateDescriptorResult.to_json()

# convert the object into a dict
array_of_ovf_create_descriptor_result_dict = array_of_ovf_create_descriptor_result_instance.to_dict()
# create an instance of ArrayOfOvfCreateDescriptorResult from a dict
array_of_ovf_create_descriptor_result_form_dict = array_of_ovf_create_descriptor_result.from_dict(array_of_ovf_create_descriptor_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


