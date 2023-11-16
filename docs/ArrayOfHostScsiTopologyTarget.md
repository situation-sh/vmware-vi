# ArrayOfHostScsiTopologyTarget

A boxed array of *HostScsiTopologyTarget*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostScsiTopologyTarget]**](HostScsiTopologyTarget.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_scsi_topology_target import ArrayOfHostScsiTopologyTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostScsiTopologyTarget from a JSON string
array_of_host_scsi_topology_target_instance = ArrayOfHostScsiTopologyTarget.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostScsiTopologyTarget.to_json()

# convert the object into a dict
array_of_host_scsi_topology_target_dict = array_of_host_scsi_topology_target_instance.to_dict()
# create an instance of ArrayOfHostScsiTopologyTarget from a dict
array_of_host_scsi_topology_target_form_dict = array_of_host_scsi_topology_target.from_dict(array_of_host_scsi_topology_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


