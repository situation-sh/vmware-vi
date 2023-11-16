# ArrayOfVirtualNVDIMMController

A boxed array of *VirtualNVDIMMController*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualNVDIMMController]**](VirtualNVDIMMController.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_nvdimm_controller import ArrayOfVirtualNVDIMMController

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualNVDIMMController from a JSON string
array_of_virtual_nvdimm_controller_instance = ArrayOfVirtualNVDIMMController.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualNVDIMMController.to_json()

# convert the object into a dict
array_of_virtual_nvdimm_controller_dict = array_of_virtual_nvdimm_controller_instance.to_dict()
# create an instance of ArrayOfVirtualNVDIMMController from a dict
array_of_virtual_nvdimm_controller_form_dict = array_of_virtual_nvdimm_controller.from_dict(array_of_virtual_nvdimm_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


