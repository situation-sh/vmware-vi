# UnmountDiskMappingRequestType

The parameters of *HostVsanSystem.UnmountDiskMapping_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**List[VsanHostDiskMapping]**](VsanHostDiskMapping.md) |  | 

## Example

```python
from vmware_vi.models.unmount_disk_mapping_request_type import UnmountDiskMappingRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnmountDiskMappingRequestType from a JSON string
unmount_disk_mapping_request_type_instance = UnmountDiskMappingRequestType.from_json(json)
# print the JSON string representation of the object
print UnmountDiskMappingRequestType.to_json()

# convert the object into a dict
unmount_disk_mapping_request_type_dict = unmount_disk_mapping_request_type_instance.to_dict()
# create an instance of UnmountDiskMappingRequestType from a dict
unmount_disk_mapping_request_type_form_dict = unmount_disk_mapping_request_type.from_dict(unmount_disk_mapping_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


