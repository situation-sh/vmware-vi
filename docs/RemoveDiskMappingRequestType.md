# RemoveDiskMappingRequestType

The parameters of *HostVsanSystem.RemoveDiskMapping_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**List[VsanHostDiskMapping]**](VsanHostDiskMapping.md) | list of disk mappings to be removed from VSAN usage.  ***Since:*** vSphere API 5.5  | 
**maintenance_spec** | [**HostMaintenanceSpec**](HostMaintenanceSpec.md) |  | [optional] 
**timeout** | **int** | Time to wait for the task to complete in seconds. If the value is less than or equal to zero, there is no timeout. The operation fails with a Timedout exception if it timed out.  | [optional] 

## Example

```python
from vmware_vi.models.remove_disk_mapping_request_type import RemoveDiskMappingRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveDiskMappingRequestType from a JSON string
remove_disk_mapping_request_type_instance = RemoveDiskMappingRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveDiskMappingRequestType.to_json()

# convert the object into a dict
remove_disk_mapping_request_type_dict = remove_disk_mapping_request_type_instance.to_dict()
# create an instance of RemoveDiskMappingRequestType from a dict
remove_disk_mapping_request_type_form_dict = remove_disk_mapping_request_type.from_dict(remove_disk_mapping_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


