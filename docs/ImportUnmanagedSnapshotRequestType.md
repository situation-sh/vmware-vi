# ImportUnmanagedSnapshotRequestType

The parameters of *VirtualDiskManager.ImportUnmanagedSnapshot*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vdisk** | **str** | \\- The name of the disk to import, either a datastore path or a URL referring to the virtual disk from which to get geometry information.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**vvol_id** | **str** | \\- unmanaged snapshot identifier  | 

## Example

```python
from vmware_vi.models.import_unmanaged_snapshot_request_type import ImportUnmanagedSnapshotRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ImportUnmanagedSnapshotRequestType from a JSON string
import_unmanaged_snapshot_request_type_instance = ImportUnmanagedSnapshotRequestType.from_json(json)
# print the JSON string representation of the object
print ImportUnmanagedSnapshotRequestType.to_json()

# convert the object into a dict
import_unmanaged_snapshot_request_type_dict = import_unmanaged_snapshot_request_type_instance.to_dict()
# create an instance of ImportUnmanagedSnapshotRequestType from a dict
import_unmanaged_snapshot_request_type_form_dict = import_unmanaged_snapshot_request_type.from_dict(import_unmanaged_snapshot_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


