# VmfsDatastoreSpec

Base class for VMFS datastore addition specification.  Used as a generic way to point to one of the creation specifications that can be used to apply a specification to effect the creation or extension of a VMFS datastore. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_uuid** | **str** | The UUID of the SCSI disk on which the VMFS datastore is located.  See also *HostScsiDisk*, *ScsiLun.uuid*.  | 

## Example

```python
from vmware_vi.models.vmfs_datastore_spec import VmfsDatastoreSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsDatastoreSpec from a JSON string
vmfs_datastore_spec_instance = VmfsDatastoreSpec.from_json(json)
# print the JSON string representation of the object
print VmfsDatastoreSpec.to_json()

# convert the object into a dict
vmfs_datastore_spec_dict = vmfs_datastore_spec_instance.to_dict()
# create an instance of VmfsDatastoreSpec from a dict
vmfs_datastore_spec_form_dict = vmfs_datastore_spec.from_dict(vmfs_datastore_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


