# ArrayOfVirtualNVDIMM

A boxed array of *VirtualNVDIMM*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualNVDIMM]**](VirtualNVDIMM.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_nvdimm import ArrayOfVirtualNVDIMM

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualNVDIMM from a JSON string
array_of_virtual_nvdimm_instance = ArrayOfVirtualNVDIMM.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualNVDIMM.to_json()

# convert the object into a dict
array_of_virtual_nvdimm_dict = array_of_virtual_nvdimm_instance.to_dict()
# create an instance of ArrayOfVirtualNVDIMM from a dict
array_of_virtual_nvdimm_form_dict = array_of_virtual_nvdimm.from_dict(array_of_virtual_nvdimm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


