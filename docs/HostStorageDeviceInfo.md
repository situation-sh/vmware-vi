# HostStorageDeviceInfo

This data object type describes the storage subsystem configuration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_bus_adapter** | [**List[HostHostBusAdapter]**](HostHostBusAdapter.md) | The list of host bus adapters available on the host.  | [optional] 
**scsi_lun** | [**List[ScsiLun]**](ScsiLun.md) | The list of SCSI logical units available on the host.  | [optional] 
**scsi_topology** | [**HostScsiTopology**](HostScsiTopology.md) |  | [optional] 
**nvme_topology** | [**HostNvmeTopology**](HostNvmeTopology.md) |  | [optional] 
**multipath_info** | [**HostMultipathInfo**](HostMultipathInfo.md) |  | [optional] 
**plug_store_topology** | [**HostPlugStoreTopology**](HostPlugStoreTopology.md) |  | [optional] 
**software_internet_scsi_enabled** | **bool** | Indicates if the software iSCSI initiator is enabled on this system  | 

## Example

```python
from vmware_vi.models.host_storage_device_info import HostStorageDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostStorageDeviceInfo from a JSON string
host_storage_device_info_instance = HostStorageDeviceInfo.from_json(json)
# print the JSON string representation of the object
print HostStorageDeviceInfo.to_json()

# convert the object into a dict
host_storage_device_info_dict = host_storage_device_info_instance.to_dict()
# create an instance of HostStorageDeviceInfo from a dict
host_storage_device_info_form_dict = host_storage_device_info.from_dict(host_storage_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


