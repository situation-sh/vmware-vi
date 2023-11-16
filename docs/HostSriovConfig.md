# HostSriovConfig

This data object allows configuration of SR-IOV device.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sriov_enabled** | **bool** | enable SR-IOV for this device  ***Since:*** vSphere API 5.5  | 
**num_virtual_function** | **int** | Number of SR-IOV virtual functions to enable on this device  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.host_sriov_config import HostSriovConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostSriovConfig from a JSON string
host_sriov_config_instance = HostSriovConfig.from_json(json)
# print the JSON string representation of the object
print HostSriovConfig.to_json()

# convert the object into a dict
host_sriov_config_dict = host_sriov_config_instance.to_dict()
# create an instance of HostSriovConfig from a dict
host_sriov_config_form_dict = host_sriov_config.from_dict(host_sriov_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


