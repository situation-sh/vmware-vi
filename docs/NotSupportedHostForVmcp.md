# NotSupportedHostForVmcp

The host does not support VM Component Protection.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The name of the host.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.not_supported_host_for_vmcp import NotSupportedHostForVmcp

# TODO update the JSON string below
json = "{}"
# create an instance of NotSupportedHostForVmcp from a JSON string
not_supported_host_for_vmcp_instance = NotSupportedHostForVmcp.from_json(json)
# print the JSON string representation of the object
print NotSupportedHostForVmcp.to_json()

# convert the object into a dict
not_supported_host_for_vmcp_dict = not_supported_host_for_vmcp_instance.to_dict()
# create an instance of NotSupportedHostForVmcp from a dict
not_supported_host_for_vmcp_form_dict = not_supported_host_for_vmcp.from_dict(not_supported_host_for_vmcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


