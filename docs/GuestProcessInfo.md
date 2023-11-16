# GuestProcessInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The process name  ***Since:*** vSphere API 5.0  | 
**pid** | **int** | The process ID  ***Since:*** vSphere API 5.0  | 
**owner** | **str** | The process owner  ***Since:*** vSphere API 5.0  | 
**cmd_line** | **str** | The full command line  ***Since:*** vSphere API 5.0  | 
**start_time** | **datetime** | The start time of the process  ***Since:*** vSphere API 5.0  | 
**end_time** | **datetime** | If the process was started using *GuestProcessManager.StartProgramInGuest* then the process completion time will be available if queried within 5 minutes after it completes.  ***Since:*** vSphere API 5.0  | [optional] 
**exit_code** | **int** | If the process was started using *GuestProcessManager.StartProgramInGuest* then the process exit code will be available if queried within 5 minutes after it completes.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.guest_process_info import GuestProcessInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestProcessInfo from a JSON string
guest_process_info_instance = GuestProcessInfo.from_json(json)
# print the JSON string representation of the object
print GuestProcessInfo.to_json()

# convert the object into a dict
guest_process_info_dict = guest_process_info_instance.to_dict()
# create an instance of GuestProcessInfo from a dict
guest_process_info_form_dict = guest_process_info.from_dict(guest_process_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


