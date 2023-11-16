# FolderFailedHostResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | Host name for which fault belongs to.  ***Since:*** vSphere API 6.7.1  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**context** | [**LocalizableMessage**](LocalizableMessage.md) |  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.folder_failed_host_result import FolderFailedHostResult

# TODO update the JSON string below
json = "{}"
# create an instance of FolderFailedHostResult from a JSON string
folder_failed_host_result_instance = FolderFailedHostResult.from_json(json)
# print the JSON string representation of the object
print FolderFailedHostResult.to_json()

# convert the object into a dict
folder_failed_host_result_dict = folder_failed_host_result_instance.to_dict()
# create an instance of FolderFailedHostResult from a dict
folder_failed_host_result_form_dict = folder_failed_host_result.from_dict(folder_failed_host_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


