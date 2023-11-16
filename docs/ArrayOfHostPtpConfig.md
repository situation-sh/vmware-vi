# ArrayOfHostPtpConfig

A boxed array of *HostPtpConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPtpConfig]**](HostPtpConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ptp_config import ArrayOfHostPtpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPtpConfig from a JSON string
array_of_host_ptp_config_instance = ArrayOfHostPtpConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPtpConfig.to_json()

# convert the object into a dict
array_of_host_ptp_config_dict = array_of_host_ptp_config_instance.to_dict()
# create an instance of ArrayOfHostPtpConfig from a dict
array_of_host_ptp_config_form_dict = array_of_host_ptp_config.from_dict(array_of_host_ptp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


