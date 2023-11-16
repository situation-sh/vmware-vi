# ArrayOfOvfCreateDescriptorParams

A boxed array of *OvfCreateDescriptorParams*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfCreateDescriptorParams]**](OvfCreateDescriptorParams.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_create_descriptor_params import ArrayOfOvfCreateDescriptorParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfCreateDescriptorParams from a JSON string
array_of_ovf_create_descriptor_params_instance = ArrayOfOvfCreateDescriptorParams.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfCreateDescriptorParams.to_json()

# convert the object into a dict
array_of_ovf_create_descriptor_params_dict = array_of_ovf_create_descriptor_params_instance.to_dict()
# create an instance of ArrayOfOvfCreateDescriptorParams from a dict
array_of_ovf_create_descriptor_params_form_dict = array_of_ovf_create_descriptor_params.from_dict(array_of_ovf_create_descriptor_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


