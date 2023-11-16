# DiskChangeExtent

An area of the disk flagged as modified  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** | Start offset (in bytes) of modified area  ***Since:*** vSphere API 4.0  | 
**length** | **int** | Length (in bytes) of modified area  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.disk_change_extent import DiskChangeExtent

# TODO update the JSON string below
json = "{}"
# create an instance of DiskChangeExtent from a JSON string
disk_change_extent_instance = DiskChangeExtent.from_json(json)
# print the JSON string representation of the object
print DiskChangeExtent.to_json()

# convert the object into a dict
disk_change_extent_dict = disk_change_extent_instance.to_dict()
# create an instance of DiskChangeExtent from a dict
disk_change_extent_form_dict = disk_change_extent.from_dict(disk_change_extent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


