# HostMultipathInfo

The *HostMultipathInfo* data object describes the multipathing policy configuration to determine the storage failover policies for a SCSI logical unit.  The multipathing policy configuration operates on SCSI logical units and the paths to the logical units.  Multipath policy configuration is only possible on storage devices provided by the native multipathing plug-store plugin. Storage devices using the native multipathing storage plugin will have an entry in this data object. Storage devices provided by a different storage plugin will not appear in the inventory represented by this data object.  Legacy note: In hosts where *HostMultipathStateInfo* is not defined or does not exist on the *HostStorageDeviceInfo* object, only native multipathing exists. That means for these hosts, the MultipathInfo object contains the complete set of LUNs and paths on the LUNs available on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun** | [**List[HostMultipathInfoLogicalUnit]**](HostMultipathInfoLogicalUnit.md) | List of logical units that can be configured for multipathing.  | [optional] 

## Example

```python
from vmware_vi.models.host_multipath_info import HostMultipathInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostMultipathInfo from a JSON string
host_multipath_info_instance = HostMultipathInfo.from_json(json)
# print the JSON string representation of the object
print HostMultipathInfo.to_json()

# convert the object into a dict
host_multipath_info_dict = host_multipath_info_instance.to_dict()
# create an instance of HostMultipathInfo from a dict
host_multipath_info_form_dict = host_multipath_info.from_dict(host_multipath_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


