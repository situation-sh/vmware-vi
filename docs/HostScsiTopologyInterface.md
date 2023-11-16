# HostScsiTopologyInterface

This data object type describes the SCSI interface that is associated with a list of targets. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The identifier for the SCSI interface  | 
**adapter** | [**HostHostBusAdapter**](HostHostBusAdapter.md) |  | 
**target** | [**List[HostScsiTopologyTarget]**](HostScsiTopologyTarget.md) | The list of targets to which the SCSI interface is associated.  | [optional] 

## Example

```python
from vmware_vi.models.host_scsi_topology_interface import HostScsiTopologyInterface

# TODO update the JSON string below
json = "{}"
# create an instance of HostScsiTopologyInterface from a JSON string
host_scsi_topology_interface_instance = HostScsiTopologyInterface.from_json(json)
# print the JSON string representation of the object
print HostScsiTopologyInterface.to_json()

# convert the object into a dict
host_scsi_topology_interface_dict = host_scsi_topology_interface_instance.to_dict()
# create an instance of HostScsiTopologyInterface from a dict
host_scsi_topology_interface_form_dict = host_scsi_topology_interface.from_dict(host_scsi_topology_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


