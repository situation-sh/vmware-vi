# HostHardwareStatusInfo

Data object representing the status of the hardware components of the host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_status_info** | [**List[HostHardwareElementInfo]**](HostHardwareElementInfo.md) | Status of the physical memory  ***Since:*** VI API 2.5  | [optional] 
**cpu_status_info** | [**List[HostHardwareElementInfo]**](HostHardwareElementInfo.md) | Status of the CPU packages  ***Since:*** VI API 2.5  | [optional] 
**storage_status_info** | [**List[HostStorageElementInfo]**](HostStorageElementInfo.md) | Status of the physical storage system  ***Since:*** VI API 2.5  | [optional] 
**dpu_status_info** | [**List[DpuStatusInfo]**](DpuStatusInfo.md) | Status of one or more DPU elements  | [optional] 

## Example

```python
from vmware_vi.models.host_hardware_status_info import HostHardwareStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostHardwareStatusInfo from a JSON string
host_hardware_status_info_instance = HostHardwareStatusInfo.from_json(json)
# print the JSON string representation of the object
print HostHardwareStatusInfo.to_json()

# convert the object into a dict
host_hardware_status_info_dict = host_hardware_status_info_instance.to_dict()
# create an instance of HostHardwareStatusInfo from a dict
host_hardware_status_info_form_dict = host_hardware_status_info.from_dict(host_hardware_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


