# HostVsanInternalSystemVsanObjectOperationResult

Operation result for a VSAN object upon failure.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The UUID of the in question VSAN object.  ***Since:*** vSphere API 6.0  | 
**failure_reason** | [**List[LocalizableMessage]**](LocalizableMessage.md) | List of LocalizableMessages with the failure vobs.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_vsan_internal_system_vsan_object_operation_result import HostVsanInternalSystemVsanObjectOperationResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostVsanInternalSystemVsanObjectOperationResult from a JSON string
host_vsan_internal_system_vsan_object_operation_result_instance = HostVsanInternalSystemVsanObjectOperationResult.from_json(json)
# print the JSON string representation of the object
print HostVsanInternalSystemVsanObjectOperationResult.to_json()

# convert the object into a dict
host_vsan_internal_system_vsan_object_operation_result_dict = host_vsan_internal_system_vsan_object_operation_result_instance.to_dict()
# create an instance of HostVsanInternalSystemVsanObjectOperationResult from a dict
host_vsan_internal_system_vsan_object_operation_result_form_dict = host_vsan_internal_system_vsan_object_operation_result.from_dict(host_vsan_internal_system_vsan_object_operation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


