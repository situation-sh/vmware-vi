# HostScsiTopologyTarget

This data object type describes the SCSI target that is associated with a list of logical units. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The identifier for the SCSI target  | 
**target** | **int** | The target identifier.  | 
**lun** | [**List[HostScsiTopologyLun]**](HostScsiTopologyLun.md) | The list of SCSI logical units with which a target is associated.  | [optional] 
**transport** | [**HostTargetTransport**](HostTargetTransport.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_scsi_topology_target import HostScsiTopologyTarget

# TODO update the JSON string below
json = "{}"
# create an instance of HostScsiTopologyTarget from a JSON string
host_scsi_topology_target_instance = HostScsiTopologyTarget.from_json(json)
# print the JSON string representation of the object
print HostScsiTopologyTarget.to_json()

# convert the object into a dict
host_scsi_topology_target_dict = host_scsi_topology_target_instance.to_dict()
# create an instance of HostScsiTopologyTarget from a dict
host_scsi_topology_target_form_dict = host_scsi_topology_target.from_dict(host_scsi_topology_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


