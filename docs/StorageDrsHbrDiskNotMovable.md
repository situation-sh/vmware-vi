# StorageDrsHbrDiskNotMovable

This fault is thrown when HMS service cannot move certain secondary replica disks per Storage DRS move recommendations  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_movable_disk_ids** | **str** | Comma-separated list of disk IDs that are not movable and failed Storage DRS recommendation action.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.storage_drs_hbr_disk_not_movable import StorageDrsHbrDiskNotMovable

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsHbrDiskNotMovable from a JSON string
storage_drs_hbr_disk_not_movable_instance = StorageDrsHbrDiskNotMovable.from_json(json)
# print the JSON string representation of the object
print StorageDrsHbrDiskNotMovable.to_json()

# convert the object into a dict
storage_drs_hbr_disk_not_movable_dict = storage_drs_hbr_disk_not_movable_instance.to_dict()
# create an instance of StorageDrsHbrDiskNotMovable from a dict
storage_drs_hbr_disk_not_movable_form_dict = storage_drs_hbr_disk_not_movable.from_dict(storage_drs_hbr_disk_not_movable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


