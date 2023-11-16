# HostPatchManagerPatchManagerOperationSpec

Optional parameters for hostd to pass to exupdate.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxy** | **str** | The name of the possible proxy for esxupdate to use to connect to a server.  The patch and metadata may be cached within the proxy server.  ***Since:*** vSphere API 4.0  | [optional] 
**port** | **int** | The port of the possible proxy for esxupdate to use to connect to a server.  The patch and metadata may be cached within the proxy server.  ***Since:*** vSphere API 4.0  | [optional] 
**user_name** | **str** | The user name used for the proxy server.  ***Since:*** vSphere API 4.0  | [optional] 
**password** | **str** | The password used for the proxy server.  This is passed with ssl through a trusted channel.  ***Since:*** vSphere API 4.0  | [optional] 
**cmd_option** | **str** | Possible command line options when calling esxupdate.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_patch_manager_patch_manager_operation_spec import HostPatchManagerPatchManagerOperationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostPatchManagerPatchManagerOperationSpec from a JSON string
host_patch_manager_patch_manager_operation_spec_instance = HostPatchManagerPatchManagerOperationSpec.from_json(json)
# print the JSON string representation of the object
print HostPatchManagerPatchManagerOperationSpec.to_json()

# convert the object into a dict
host_patch_manager_patch_manager_operation_spec_dict = host_patch_manager_patch_manager_operation_spec_instance.to_dict()
# create an instance of HostPatchManagerPatchManagerOperationSpec from a dict
host_patch_manager_patch_manager_operation_spec_form_dict = host_patch_manager_patch_manager_operation_spec.from_dict(host_patch_manager_patch_manager_operation_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


