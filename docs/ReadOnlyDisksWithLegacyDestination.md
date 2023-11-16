# ReadOnlyDisksWithLegacyDestination

The virtual machine uses read-only (undoable or nonpersistent) disks that can cause a slower power on at the migration destination.  As a result, VMtion could slow down considerably or timeout. This is an issue only for migration of powered-on virtual machines from an ESX host with version greater than 2.0.x to an ESX host with version 2.0.x. It will be an error if the number of such disks is great enough to cause timeout ( &ge; 3 ), or a warning otherwise. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ro_disk_count** | **int** | The number of read-only disks in use.  | 
**timeout_danger** | **bool** | Whether this number of disks will cause a timeout failure.  | 

## Example

```python
from vmware_vi.models.read_only_disks_with_legacy_destination import ReadOnlyDisksWithLegacyDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ReadOnlyDisksWithLegacyDestination from a JSON string
read_only_disks_with_legacy_destination_instance = ReadOnlyDisksWithLegacyDestination.from_json(json)
# print the JSON string representation of the object
print ReadOnlyDisksWithLegacyDestination.to_json()

# convert the object into a dict
read_only_disks_with_legacy_destination_dict = read_only_disks_with_legacy_destination_instance.to_dict()
# create an instance of ReadOnlyDisksWithLegacyDestination from a dict
read_only_disks_with_legacy_destination_form_dict = read_only_disks_with_legacy_destination.from_dict(read_only_disks_with_legacy_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


