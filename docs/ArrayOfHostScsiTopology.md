# ArrayOfHostScsiTopology

A boxed array of *HostScsiTopology*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostScsiTopology]**](HostScsiTopology.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_scsi_topology import ArrayOfHostScsiTopology

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostScsiTopology from a JSON string
array_of_host_scsi_topology_instance = ArrayOfHostScsiTopology.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostScsiTopology.to_json()

# convert the object into a dict
array_of_host_scsi_topology_dict = array_of_host_scsi_topology_instance.to_dict()
# create an instance of ArrayOfHostScsiTopology from a dict
array_of_host_scsi_topology_form_dict = array_of_host_scsi_topology.from_dict(array_of_host_scsi_topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


