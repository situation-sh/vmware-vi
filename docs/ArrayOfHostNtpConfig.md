# ArrayOfHostNtpConfig

A boxed array of *HostNtpConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNtpConfig]**](HostNtpConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ntp_config import ArrayOfHostNtpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNtpConfig from a JSON string
array_of_host_ntp_config_instance = ArrayOfHostNtpConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNtpConfig.to_json()

# convert the object into a dict
array_of_host_ntp_config_dict = array_of_host_ntp_config_instance.to_dict()
# create an instance of ArrayOfHostNtpConfig from a dict
array_of_host_ntp_config_form_dict = array_of_host_ntp_config.from_dict(array_of_host_ntp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


