# VirtualNVDIMMController

The Virtual NVDIMM controller.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_nvdimm_controller import VirtualNVDIMMController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNVDIMMController from a JSON string
virtual_nvdimm_controller_instance = VirtualNVDIMMController.from_json(json)
# print the JSON string representation of the object
print VirtualNVDIMMController.to_json()

# convert the object into a dict
virtual_nvdimm_controller_dict = virtual_nvdimm_controller_instance.to_dict()
# create an instance of VirtualNVDIMMController from a dict
virtual_nvdimm_controller_form_dict = virtual_nvdimm_controller.from_dict(virtual_nvdimm_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


