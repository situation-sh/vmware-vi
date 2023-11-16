# HostScsiTopologyLun

This data object type describes the SCSI logical unit. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The identifier for the SCSI Lun  | 
**lun** | **int** | The logical unit number of the SCSI logical unit.  | 
**scsi_lun** | [**ScsiLun**](ScsiLun.md) |  | 

## Example

```python
from vmware_vi.models.host_scsi_topology_lun import HostScsiTopologyLun

# TODO update the JSON string below
json = "{}"
# create an instance of HostScsiTopologyLun from a JSON string
host_scsi_topology_lun_instance = HostScsiTopologyLun.from_json(json)
# print the JSON string representation of the object
print HostScsiTopologyLun.to_json()

# convert the object into a dict
host_scsi_topology_lun_dict = host_scsi_topology_lun_instance.to_dict()
# create an instance of HostScsiTopologyLun from a dict
host_scsi_topology_lun_form_dict = host_scsi_topology_lun.from_dict(host_scsi_topology_lun_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


