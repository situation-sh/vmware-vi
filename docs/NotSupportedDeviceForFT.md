# NotSupportedDeviceForFT

Deprecated as of vSphere API 7.0. Not used since vSphere API 6.5.  VMs with pvscsi or vmxnet3 virtual devices support Fault Tolerance only on 4.1 or later hosts.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host_name** | **str** | The host name  ***Since:*** vSphere API 4.1  | [optional] 
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**vm_name** | **str** | The virtual machine name  ***Since:*** vSphere API 4.1  | [optional] 
**device_type** | **str** | The device type  ***Since:*** vSphere API 4.1  | 
**device_label** | **str** | The device label  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.not_supported_device_for_ft import NotSupportedDeviceForFT

# TODO update the JSON string below
json = "{}"
# create an instance of NotSupportedDeviceForFT from a JSON string
not_supported_device_for_ft_instance = NotSupportedDeviceForFT.from_json(json)
# print the JSON string representation of the object
print NotSupportedDeviceForFT.to_json()

# convert the object into a dict
not_supported_device_for_ft_dict = not_supported_device_for_ft_instance.to_dict()
# create an instance of NotSupportedDeviceForFT from a dict
not_supported_device_for_ft_form_dict = not_supported_device_for_ft.from_dict(not_supported_device_for_ft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


