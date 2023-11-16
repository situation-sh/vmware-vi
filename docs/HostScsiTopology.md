# HostScsiTopology

This data object type describes the SCSI topology information.  The data objects in this data object type model the SCSI storage objects from a topological point of view. The SCSI topological view organizes objects by SCSI interface, which contain targets, which in turn contain logical units.  SCSI Topology information is not guaranteed to exhaustively enumerate all storage devices on the system. It only shows storage devices that are actually enumerable from a host bus adapter. This means that only storage devices that are composed from one or more paths, which are in turn provided by a host bus adapter, will appear in this inventory.  Storage devices provided by the native multipathing plugin (NMP) will always be represented in this inventory since NMP uses a simple policy to create devices out of the paths it claims.  Examples of storage devices that will not appear in this inventory are logical devices that are not formed from directly claiming paths. Specific examples of devices that will not appear in this inventory include a device backed by a ramdisk or formed from a software RAID plugin.  Legacy note: In hosts where *HostPlugStoreTopology* is not defined or does not exist on the *HostStorageDeviceInfo* object, only native multipathing exists. That means for these hosts, the ScsiTopology object contains the complete set of LUNs and targets available on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter** | [**List[HostScsiTopologyInterface]**](HostScsiTopologyInterface.md) | The list of SCSI interfaces.  | [optional] 

## Example

```python
from vmware_vi.models.host_scsi_topology import HostScsiTopology

# TODO update the JSON string below
json = "{}"
# create an instance of HostScsiTopology from a JSON string
host_scsi_topology_instance = HostScsiTopology.from_json(json)
# print the JSON string representation of the object
print HostScsiTopology.to_json()

# convert the object into a dict
host_scsi_topology_dict = host_scsi_topology_instance.to_dict()
# create an instance of HostScsiTopology from a dict
host_scsi_topology_form_dict = host_scsi_topology.from_dict(host_scsi_topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


