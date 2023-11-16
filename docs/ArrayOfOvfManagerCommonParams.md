# ArrayOfOvfManagerCommonParams

A boxed array of *OvfManagerCommonParams*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfManagerCommonParams]**](OvfManagerCommonParams.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_manager_common_params import ArrayOfOvfManagerCommonParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfManagerCommonParams from a JSON string
array_of_ovf_manager_common_params_instance = ArrayOfOvfManagerCommonParams.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfManagerCommonParams.to_json()

# convert the object into a dict
array_of_ovf_manager_common_params_dict = array_of_ovf_manager_common_params_instance.to_dict()
# create an instance of ArrayOfOvfManagerCommonParams from a dict
array_of_ovf_manager_common_params_form_dict = array_of_ovf_manager_common_params.from_dict(array_of_ovf_manager_common_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


