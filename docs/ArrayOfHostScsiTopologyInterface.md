# ArrayOfHostScsiTopologyInterface

A boxed array of *HostScsiTopologyInterface*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostScsiTopologyInterface]**](HostScsiTopologyInterface.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_scsi_topology_interface import ArrayOfHostScsiTopologyInterface

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostScsiTopologyInterface from a JSON string
array_of_host_scsi_topology_interface_instance = ArrayOfHostScsiTopologyInterface.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostScsiTopologyInterface.to_json()

# convert the object into a dict
array_of_host_scsi_topology_interface_dict = array_of_host_scsi_topology_interface_instance.to_dict()
# create an instance of ArrayOfHostScsiTopologyInterface from a dict
array_of_host_scsi_topology_interface_form_dict = array_of_host_scsi_topology_interface.from_dict(array_of_host_scsi_topology_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


