# VmFailedRelayoutOnVmfs2DatastoreEvent

This event records a failure to relay out a virtual machine when the virtual machine still has disks on a VMFS2 volume. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_failed_relayout_on_vmfs2_datastore_event import VmFailedRelayoutOnVmfs2DatastoreEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFailedRelayoutOnVmfs2DatastoreEvent from a JSON string
vm_failed_relayout_on_vmfs2_datastore_event_instance = VmFailedRelayoutOnVmfs2DatastoreEvent.from_json(json)
# print the JSON string representation of the object
print VmFailedRelayoutOnVmfs2DatastoreEvent.to_json()

# convert the object into a dict
vm_failed_relayout_on_vmfs2_datastore_event_dict = vm_failed_relayout_on_vmfs2_datastore_event_instance.to_dict()
# create an instance of VmFailedRelayoutOnVmfs2DatastoreEvent from a dict
vm_failed_relayout_on_vmfs2_datastore_event_form_dict = vm_failed_relayout_on_vmfs2_datastore_event.from_dict(vm_failed_relayout_on_vmfs2_datastore_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


