# HostPatchManagerResult

The result of the operation.  Some of the fields are only valid for specific operations.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the scan result schema.  ***Since:*** vSphere API 4.0  | 
**status** | [**List[HostPatchManagerStatus]**](HostPatchManagerStatus.md) | The scan results for each patch.  ***Since:*** vSphere API 4.0  | [optional] 
**xml_result** | **str** | The scan results in XML format.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_patch_manager_result import HostPatchManagerResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostPatchManagerResult from a JSON string
host_patch_manager_result_instance = HostPatchManagerResult.from_json(json)
# print the JSON string representation of the object
print HostPatchManagerResult.to_json()

# convert the object into a dict
host_patch_manager_result_dict = host_patch_manager_result_instance.to_dict()
# create an instance of HostPatchManagerResult from a dict
host_patch_manager_result_form_dict = host_patch_manager_result.from_dict(host_patch_manager_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


