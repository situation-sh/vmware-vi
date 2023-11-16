# HostConfigureVFlashResourceRequestType

The parameters of *HostVFlashManager.HostConfigureVFlashResource*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostVFlashManagerVFlashResourceConfigSpec**](HostVFlashManagerVFlashResourceConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_configure_v_flash_resource_request_type import HostConfigureVFlashResourceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigureVFlashResourceRequestType from a JSON string
host_configure_v_flash_resource_request_type_instance = HostConfigureVFlashResourceRequestType.from_json(json)
# print the JSON string representation of the object
print HostConfigureVFlashResourceRequestType.to_json()

# convert the object into a dict
host_configure_v_flash_resource_request_type_dict = host_configure_v_flash_resource_request_type_instance.to_dict()
# create an instance of HostConfigureVFlashResourceRequestType from a dict
host_configure_v_flash_resource_request_type_form_dict = host_configure_v_flash_resource_request_type.from_dict(host_configure_v_flash_resource_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


