# VmfsDatastoreAllExtentOption

Datastore addition policy to use the entire disk as a single extent for a VMFS datastore.  If there is any data on the disk, it will be overwritten. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vmfs_datastore_all_extent_option import VmfsDatastoreAllExtentOption

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsDatastoreAllExtentOption from a JSON string
vmfs_datastore_all_extent_option_instance = VmfsDatastoreAllExtentOption.from_json(json)
# print the JSON string representation of the object
print VmfsDatastoreAllExtentOption.to_json()

# convert the object into a dict
vmfs_datastore_all_extent_option_dict = vmfs_datastore_all_extent_option_instance.to_dict()
# create an instance of VmfsDatastoreAllExtentOption from a dict
vmfs_datastore_all_extent_option_form_dict = vmfs_datastore_all_extent_option.from_dict(vmfs_datastore_all_extent_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


