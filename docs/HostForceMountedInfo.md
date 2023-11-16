# HostForceMountedInfo

When the system detects a copy of a VmfsVolume, it will not be auto-mounted on the host and it will be detected as 'UnresolvedVmfsVolume'.  If user decides to keep the original Uuid and mount it on the host, it will have 'forceMounted' flag and 'forceMountedInfo' set. 'ForceMountedInfo' provides additional information specific to user-mounted VmfsVolume.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persist** | **bool** | Indicates if the vmfsExtent information persistent across host reboots.  ***Since:*** vSphere API 4.0  | 
**mounted** | **bool** | Indicates if the volume is currently mounted on the host  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.host_force_mounted_info import HostForceMountedInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostForceMountedInfo from a JSON string
host_force_mounted_info_instance = HostForceMountedInfo.from_json(json)
# print the JSON string representation of the object
print HostForceMountedInfo.to_json()

# convert the object into a dict
host_force_mounted_info_dict = host_force_mounted_info_instance.to_dict()
# create an instance of HostForceMountedInfo from a dict
host_force_mounted_info_form_dict = host_force_mounted_info.from_dict(host_force_mounted_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


