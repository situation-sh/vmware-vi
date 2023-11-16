# DiskChangeInfo

Data structure to describe areas in a disk associated with this VM that have been modified since a well-defined point in the past.  Returned by *VirtualMachine.QueryChangedDiskAreas*. This data structure describes a subset of the disk identified by startOffset and length. All areas that have been modified within this interval are listed under changedArea.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_offset** | **int** | Start offset (in bytes) of disk area described by this data structure.  ***Since:*** vSphere API 4.0  | 
**length** | **int** | Length (in bytes) of disk area described by this data structure.  ***Since:*** vSphere API 4.0  | 
**changed_area** | [**List[DiskChangeExtent]**](DiskChangeExtent.md) | Modified disk areas.  Might be empty if no parts of the disk between startOffset and startOffset + length were modified.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.disk_change_info import DiskChangeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DiskChangeInfo from a JSON string
disk_change_info_instance = DiskChangeInfo.from_json(json)
# print the JSON string representation of the object
print DiskChangeInfo.to_json()

# convert the object into a dict
disk_change_info_dict = disk_change_info_instance.to_dict()
# create an instance of DiskChangeInfo from a dict
disk_change_info_form_dict = disk_change_info.from_dict(disk_change_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


