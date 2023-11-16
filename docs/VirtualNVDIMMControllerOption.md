# VirtualNVDIMMControllerOption

VirtualNVDIMMControllerOption is the data object that contains the options for a virtual NVDIMM controller.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_nvdimm_controllers** | [**IntOption**](IntOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_nvdimm_controller_option import VirtualNVDIMMControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNVDIMMControllerOption from a JSON string
virtual_nvdimm_controller_option_instance = VirtualNVDIMMControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualNVDIMMControllerOption.to_json()

# convert the object into a dict
virtual_nvdimm_controller_option_dict = virtual_nvdimm_controller_option_instance.to_dict()
# create an instance of VirtualNVDIMMControllerOption from a dict
virtual_nvdimm_controller_option_form_dict = virtual_nvdimm_controller_option.from_dict(virtual_nvdimm_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


