# HostResignatureRescanResult

The *HostResignatureRescanResult* data object identifies the newly created volume that is the result of a resignature operation.  This data object is contained in the task object returned by the *HostDatastoreSystem.ResignatureUnresolvedVmfsVolume_Task* method.  When a client calls the resignature method, the Server resignatures the volume, rescans the specified list of hosts, and auto-mounts the volume on the other hosts that share the same underlying storage LUNs.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rescan** | [**List[HostVmfsRescanResult]**](HostVmfsRescanResult.md) | Deprecated as of vSphere API 5.1, the results of the operation are available when the task completes. That is, for shared volumes, the new volume is mounted on all of the connected hosts.  List of VMFS Rescan operation results.  ***Since:*** vSphere API 4.0  | [optional] 
**result** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_resignature_rescan_result import HostResignatureRescanResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostResignatureRescanResult from a JSON string
host_resignature_rescan_result_instance = HostResignatureRescanResult.from_json(json)
# print the JSON string representation of the object
print HostResignatureRescanResult.to_json()

# convert the object into a dict
host_resignature_rescan_result_dict = host_resignature_rescan_result_instance.to_dict()
# create an instance of HostResignatureRescanResult from a dict
host_resignature_rescan_result_form_dict = host_resignature_rescan_result.from_dict(host_resignature_rescan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


