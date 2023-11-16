# HostSriovInfo

This data object provides information about the state of SR-IOV device.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sriov_enabled** | **bool** | Whether SRIOV has been enabled by the user  ***Since:*** vSphere API 5.5  | 
**sriov_capable** | **bool** | Whether SRIOV is possible for this device  ***Since:*** vSphere API 5.5  | 
**sriov_active** | **bool** | Whether SRIOV is active for this device (meaning enabled + rebooted)  ***Since:*** vSphere API 5.5  | 
**num_virtual_function_requested** | **int** | Number of SRIOV virtual functions requested for this device  ***Since:*** vSphere API 5.5  | 
**num_virtual_function** | **int** | Number of SRIOV virtual functions present on this device  ***Since:*** vSphere API 5.5  | 
**max_virtual_function_supported** | **int** | Maximum number of SRIOV virtual functions supported on this device  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.host_sriov_info import HostSriovInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSriovInfo from a JSON string
host_sriov_info_instance = HostSriovInfo.from_json(json)
# print the JSON string representation of the object
print HostSriovInfo.to_json()

# convert the object into a dict
host_sriov_info_dict = host_sriov_info_instance.to_dict()
# create an instance of HostSriovInfo from a dict
host_sriov_info_form_dict = host_sriov_info.from_dict(host_sriov_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


