# ArrayOfHostPtpConfigPtpPort

A boxed array of *HostPtpConfigPtpPort*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPtpConfigPtpPort]**](HostPtpConfigPtpPort.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ptp_config_ptp_port import ArrayOfHostPtpConfigPtpPort

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPtpConfigPtpPort from a JSON string
array_of_host_ptp_config_ptp_port_instance = ArrayOfHostPtpConfigPtpPort.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPtpConfigPtpPort.to_json()

# convert the object into a dict
array_of_host_ptp_config_ptp_port_dict = array_of_host_ptp_config_ptp_port_instance.to_dict()
# create an instance of ArrayOfHostPtpConfigPtpPort from a dict
array_of_host_ptp_config_ptp_port_form_dict = array_of_host_ptp_config_ptp_port.from_dict(array_of_host_ptp_config_ptp_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


