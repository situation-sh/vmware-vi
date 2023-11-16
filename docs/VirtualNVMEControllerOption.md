# VirtualNVMEControllerOption

VirtualNVMEControllerOption is the data object that contains the options for a virtual NVME controller.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_nvme_disks** | [**IntOption**](IntOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_nvme_controller_option import VirtualNVMEControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNVMEControllerOption from a JSON string
virtual_nvme_controller_option_instance = VirtualNVMEControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualNVMEControllerOption.to_json()

# convert the object into a dict
virtual_nvme_controller_option_dict = virtual_nvme_controller_option_instance.to_dict()
# create an instance of VirtualNVMEControllerOption from a dict
virtual_nvme_controller_option_form_dict = virtual_nvme_controller_option.from_dict(virtual_nvme_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


