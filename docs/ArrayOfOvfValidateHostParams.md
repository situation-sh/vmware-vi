# ArrayOfOvfValidateHostParams

A boxed array of *OvfValidateHostParams*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfValidateHostParams]**](OvfValidateHostParams.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_validate_host_params import ArrayOfOvfValidateHostParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfValidateHostParams from a JSON string
array_of_ovf_validate_host_params_instance = ArrayOfOvfValidateHostParams.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfValidateHostParams.to_json()

# convert the object into a dict
array_of_ovf_validate_host_params_dict = array_of_ovf_validate_host_params_instance.to_dict()
# create an instance of ArrayOfOvfValidateHostParams from a dict
array_of_ovf_validate_host_params_form_dict = array_of_ovf_validate_host_params.from_dict(array_of_ovf_validate_host_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


