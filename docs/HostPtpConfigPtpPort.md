# HostPtpConfigPtpPort

Configuration of a PTP port, a logical entity providing an interface to the network for sending and receiving PTP messages with timestamping.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index into the list of PTP ports.  Supported values are in the range 0 through *HostCapability.maxSupportedPtpPorts*-1.  ***Since:*** vSphere API 7.0.3.0  | 
**device_type** | **str** | Type of network device to be used with this port.  See *HostPtpConfigDeviceType_enum* for supported values. A device type of *none* indicates that this port is inactive.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**device** | **str** | Name of PTP capable network device to be used with this port.  Supported values depend on the type of network device used. For *virtualNic* this field is the name of a valid virtual NIC. See *HostVirtualNic*. For *pciPassthruNic* this field is a valid PCI device ID composed of \&quot;bus:slot.function\&quot;, enabled for PCI passthru. See *HostPciPassthruInfo*. For *none* this field is ignored.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**ip_config** | [**HostIpConfig**](HostIpConfig.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_ptp_config_ptp_port import HostPtpConfigPtpPort

# TODO update the JSON string below
json = "{}"
# create an instance of HostPtpConfigPtpPort from a JSON string
host_ptp_config_ptp_port_instance = HostPtpConfigPtpPort.from_json(json)
# print the JSON string representation of the object
print HostPtpConfigPtpPort.to_json()

# convert the object into a dict
host_ptp_config_ptp_port_dict = host_ptp_config_ptp_port_instance.to_dict()
# create an instance of HostPtpConfigPtpPort from a dict
host_ptp_config_ptp_port_form_dict = host_ptp_config_ptp_port.from_dict(host_ptp_config_ptp_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


