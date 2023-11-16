# FilesystemQuiesceFault

This fault is thrown when creating a quiesced snapshot failed because the create snapshot operation exceeded the time limit for holding off I/O in the frozen VM.  This indicates that when we attempted to thaw the VM after creating the snapshot, we got an error back indicating that the VM was not frozen anymore. In this case, we roll back the entire snapshot create operation and throw this exception. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.filesystem_quiesce_fault import FilesystemQuiesceFault

# TODO update the JSON string below
json = "{}"
# create an instance of FilesystemQuiesceFault from a JSON string
filesystem_quiesce_fault_instance = FilesystemQuiesceFault.from_json(json)
# print the JSON string representation of the object
print FilesystemQuiesceFault.to_json()

# convert the object into a dict
filesystem_quiesce_fault_dict = filesystem_quiesce_fault_instance.to_dict()
# create an instance of FilesystemQuiesceFault from a dict
filesystem_quiesce_fault_form_dict = filesystem_quiesce_fault.from_dict(filesystem_quiesce_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


