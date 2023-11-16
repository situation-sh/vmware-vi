# ArrayOfVirtualTPMOption

A boxed array of *VirtualTPMOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualTPMOption]**](VirtualTPMOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_tpm_option import ArrayOfVirtualTPMOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualTPMOption from a JSON string
array_of_virtual_tpm_option_instance = ArrayOfVirtualTPMOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualTPMOption.to_json()

# convert the object into a dict
array_of_virtual_tpm_option_dict = array_of_virtual_tpm_option_instance.to_dict()
# create an instance of ArrayOfVirtualTPMOption from a dict
array_of_virtual_tpm_option_form_dict = array_of_virtual_tpm_option.from_dict(array_of_virtual_tpm_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


