# HostPtpConfig

Configuration information for the host PTP (Precision Time Protocol) service.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **int** | PTP domain number as defined in the IEEE 1588 standard.  Supported values are in the range 0-255.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**port** | [**List[HostPtpConfigPtpPort]**](HostPtpConfigPtpPort.md) | List of PTP port configurations.  See *HostPtpConfigPtpPort*.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.host_ptp_config import HostPtpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostPtpConfig from a JSON string
host_ptp_config_instance = HostPtpConfig.from_json(json)
# print the JSON string representation of the object
print HostPtpConfig.to_json()

# convert the object into a dict
host_ptp_config_dict = host_ptp_config_instance.to_dict()
# create an instance of HostPtpConfig from a dict
host_ptp_config_form_dict = host_ptp_config.from_dict(host_ptp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


