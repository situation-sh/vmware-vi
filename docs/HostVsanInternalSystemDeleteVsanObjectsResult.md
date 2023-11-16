# HostVsanInternalSystemDeleteVsanObjectsResult

Result of DeleteVsanObjects.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | UUID of the VSAN object.  ***Since:*** vSphere API 5.5  | 
**success** | **bool** | Indicates success or failure of object deletion.  ***Since:*** vSphere API 5.5  | 
**failure_reason** | [**List[LocalizableMessage]**](LocalizableMessage.md) | List of LocalizableMessages with the failure vobs.  This is unset if delete is successful.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.host_vsan_internal_system_delete_vsan_objects_result import HostVsanInternalSystemDeleteVsanObjectsResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostVsanInternalSystemDeleteVsanObjectsResult from a JSON string
host_vsan_internal_system_delete_vsan_objects_result_instance = HostVsanInternalSystemDeleteVsanObjectsResult.from_json(json)
# print the JSON string representation of the object
print HostVsanInternalSystemDeleteVsanObjectsResult.to_json()

# convert the object into a dict
host_vsan_internal_system_delete_vsan_objects_result_dict = host_vsan_internal_system_delete_vsan_objects_result_instance.to_dict()
# create an instance of HostVsanInternalSystemDeleteVsanObjectsResult from a dict
host_vsan_internal_system_delete_vsan_objects_result_form_dict = host_vsan_internal_system_delete_vsan_objects_result.from_dict(host_vsan_internal_system_delete_vsan_objects_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


