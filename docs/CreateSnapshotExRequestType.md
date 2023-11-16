# CreateSnapshotExRequestType

The parameters of *VirtualMachine.CreateSnapshotEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for this snapshot. The name need not be unique for this virtual machine.  | 
**description** | **str** | A description for this snapshot. If omitted, a default description may be provided.  | [optional] 
**memory** | **bool** | If TRUE, a dump of the internal state of the virtual machine (basically a memory dump) is included in the snapshot. Memory snapshots consume time and resources, and thus take longer to create. When set to FALSE, the power state of the snapshot is set to powered off.  *capabilities* indicates whether or not this virtual machine supports this operation. For a virtual machine in suspended state we always include memory unless *VirtualMachineCapability.diskOnlySnapshotOnSuspendedVMSupported* is true.  | 
**quiesce_spec** | [**VirtualMachineGuestQuiesceSpec**](VirtualMachineGuestQuiesceSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.create_snapshot_ex_request_type import CreateSnapshotExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshotExRequestType from a JSON string
create_snapshot_ex_request_type_instance = CreateSnapshotExRequestType.from_json(json)
# print the JSON string representation of the object
print CreateSnapshotExRequestType.to_json()

# convert the object into a dict
create_snapshot_ex_request_type_dict = create_snapshot_ex_request_type_instance.to_dict()
# create an instance of CreateSnapshotExRequestType from a dict
create_snapshot_ex_request_type_form_dict = create_snapshot_ex_request_type.from_dict(create_snapshot_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


