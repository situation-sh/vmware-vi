# ArrayOfVirtualNVDIMMOption

A boxed array of *VirtualNVDIMMOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualNVDIMMOption]**](VirtualNVDIMMOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_nvdimm_option import ArrayOfVirtualNVDIMMOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualNVDIMMOption from a JSON string
array_of_virtual_nvdimm_option_instance = ArrayOfVirtualNVDIMMOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualNVDIMMOption.to_json()

# convert the object into a dict
array_of_virtual_nvdimm_option_dict = array_of_virtual_nvdimm_option_instance.to_dict()
# create an instance of ArrayOfVirtualNVDIMMOption from a dict
array_of_virtual_nvdimm_option_form_dict = array_of_virtual_nvdimm_option.from_dict(array_of_virtual_nvdimm_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


