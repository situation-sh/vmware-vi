# ConfigureVFlashResourceExRequestType

The parameters of *HostVFlashManager.ConfigureVFlashResourceEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **List[str]** | An array of device path names that identify disks. See *ScsiDisk*.  | [optional] 

## Example

```python
from vmware_vi.models.configure_v_flash_resource_ex_request_type import ConfigureVFlashResourceExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureVFlashResourceExRequestType from a JSON string
configure_v_flash_resource_ex_request_type_instance = ConfigureVFlashResourceExRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigureVFlashResourceExRequestType.to_json()

# convert the object into a dict
configure_v_flash_resource_ex_request_type_dict = configure_v_flash_resource_ex_request_type_instance.to_dict()
# create an instance of ConfigureVFlashResourceExRequestType from a dict
configure_v_flash_resource_ex_request_type_form_dict = configure_v_flash_resource_ex_request_type.from_dict(configure_v_flash_resource_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


