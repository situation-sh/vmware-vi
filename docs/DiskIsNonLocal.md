# DiskIsNonLocal

Fault used for disks which are ineligible for VSAN because they are considered non-local.  See also *HostVsanSystem.QueryDisksForVsan*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.disk_is_non_local import DiskIsNonLocal

# TODO update the JSON string below
json = "{}"
# create an instance of DiskIsNonLocal from a JSON string
disk_is_non_local_instance = DiskIsNonLocal.from_json(json)
# print the JSON string representation of the object
print DiskIsNonLocal.to_json()

# convert the object into a dict
disk_is_non_local_dict = disk_is_non_local_instance.to_dict()
# create an instance of DiskIsNonLocal from a dict
disk_is_non_local_form_dict = disk_is_non_local.from_dict(disk_is_non_local_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


