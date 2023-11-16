# RDMPointsToInaccessibleDisk

One of the virtual machine's virtual disks is a Raw Disk Mapping that is itself accessible, but points to a LUN that is inaccessible. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.rdm_points_to_inaccessible_disk import RDMPointsToInaccessibleDisk

# TODO update the JSON string below
json = "{}"
# create an instance of RDMPointsToInaccessibleDisk from a JSON string
rdm_points_to_inaccessible_disk_instance = RDMPointsToInaccessibleDisk.from_json(json)
# print the JSON string representation of the object
print RDMPointsToInaccessibleDisk.to_json()

# convert the object into a dict
rdm_points_to_inaccessible_disk_dict = rdm_points_to_inaccessible_disk_instance.to_dict()
# create an instance of RDMPointsToInaccessibleDisk from a dict
rdm_points_to_inaccessible_disk_form_dict = rdm_points_to_inaccessible_disk.from_dict(rdm_points_to_inaccessible_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


