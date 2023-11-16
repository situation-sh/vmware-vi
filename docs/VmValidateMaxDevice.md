# VmValidateMaxDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device  ***Since:*** vSphere API 4.0  | 
**max** | **int** | max count for the device  ***Since:*** vSphere API 4.0  | 
**count** | **int** | number of devices found in vim.vm.ConfigSpec  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.vm_validate_max_device import VmValidateMaxDevice

# TODO update the JSON string below
json = "{}"
# create an instance of VmValidateMaxDevice from a JSON string
vm_validate_max_device_instance = VmValidateMaxDevice.from_json(json)
# print the JSON string representation of the object
print VmValidateMaxDevice.to_json()

# convert the object into a dict
vm_validate_max_device_dict = vm_validate_max_device_instance.to_dict()
# create an instance of VmValidateMaxDevice from a dict
vm_validate_max_device_form_dict = vm_validate_max_device.from_dict(vm_validate_max_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


