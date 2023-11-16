# NotSupportedHostForVmemFile

The host does not support VM Component Protection.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The name of the host.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.not_supported_host_for_vmem_file import NotSupportedHostForVmemFile

# TODO update the JSON string below
json = "{}"
# create an instance of NotSupportedHostForVmemFile from a JSON string
not_supported_host_for_vmem_file_instance = NotSupportedHostForVmemFile.from_json(json)
# print the JSON string representation of the object
print NotSupportedHostForVmemFile.to_json()

# convert the object into a dict
not_supported_host_for_vmem_file_dict = not_supported_host_for_vmem_file_instance.to_dict()
# create an instance of NotSupportedHostForVmemFile from a dict
not_supported_host_for_vmem_file_form_dict = not_supported_host_for_vmem_file.from_dict(not_supported_host_for_vmem_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


