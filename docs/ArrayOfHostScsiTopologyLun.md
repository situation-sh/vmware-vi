# ArrayOfHostScsiTopologyLun

A boxed array of *HostScsiTopologyLun*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostScsiTopologyLun]**](HostScsiTopologyLun.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_scsi_topology_lun import ArrayOfHostScsiTopologyLun

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostScsiTopologyLun from a JSON string
array_of_host_scsi_topology_lun_instance = ArrayOfHostScsiTopologyLun.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostScsiTopologyLun.to_json()

# convert the object into a dict
array_of_host_scsi_topology_lun_dict = array_of_host_scsi_topology_lun_instance.to_dict()
# create an instance of ArrayOfHostScsiTopologyLun from a dict
array_of_host_scsi_topology_lun_form_dict = array_of_host_scsi_topology_lun.from_dict(array_of_host_scsi_topology_lun_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


